from fastai.tabular.all import *
from fastai.vision.all import *
import os
import glob
import pandas as pd
from random import shuffle
import urllib.request
import streamlit as st

def img_price(o):
    for i, row in df.iterrows():
        if row[0]==os.path.basename(o): return row[2]

MODEL_IMG_URL = "https://github.com/pradrattana/anime_price_predict/raw/main/models/img_reg.pkl"
MODEL_CSV_URL = "https://github.com/pradrattana/anime_price_predict/raw/main/models/csv_reg.pkl"
urllib.request.urlretrieve(MODEL_IMG_URL, "img_reg.pkl")
urllib.request.urlretrieve(MODEL_CSV_URL, "csv_reg.pkl")
learn_img = load_learner('img_reg.pkl', cpu=True)
learn_csv = load_learner('csv_reg.pkl', cpu=True)
df = None

##################################

st.sidebar.write('### Enter an anime commission image to request a suggested price')
option = st.sidebar.radio('', ['Use a validation image', 'Use your own image'])
valid_images = glob.glob('test/*')
shuffle(valid_images)

if option == 'Use a validation image':
    st.sidebar.write('### Select a validation image')
    fname = st.sidebar.selectbox('', valid_images)
else:
    st.sidebar.write('### Select an image to upload')
    fname = st.sidebar.file_uploader('',
                                     type=['png', 'jpg', 'jpeg'],
                                     accept_multiple_files=False)
    st.sidebar.write('### Want to sell on https://artistsnclients.com/ ?')
    yn = st.sidebar.radio('', ['Yes', 'No'], 1)
    if yn == 'Yes':
        st.sidebar.write('#### Please fill in the following details')
        duration = st.sidebar.slider('Duraion', min_value=0, max_value=100, step=1)
        size = st.sidebar.radio('Size', ['Chibi', 'Portrait/Bust up', 'Half body/Knee up', 'Full body'])
        color = st.sidebar.radio('Color', ['Monochrome', 'Color'])
        background = st.sidebar.radio('Background', ['Simple/No', 'Detail'])
        like = st.sidebar.slider('Like', min_value=0, max_value=100, step=1)
        completed = st.sidebar.slider('Completed', min_value=0, max_value=200, step=1)
        size = ['Chibi', 'Portrait/Bust up', 'Half body/Knee up', 'Full body'].index(size) +1
        color = ['Monochrome', 'Color'].index(color)
        background = ['Simple/No', 'Detail'].index(background)
        data = {'size': size, 'color': color, 'bg': background, 'day': duration, 'like': like, 'completed': completed}
        df = pd.DataFrame(data=data, index=[0])
        print(df)
    if fname is None:
        fname = valid_images[0]

##################################

st.title("Suggested Price for Anime Commission")

def predict(img, df):
    predict_img = float(learn_img.predict(img)[1])
    predict_csv = predict_img if df is None else float(learn_csv.predict(df.iloc[0])[1])
    price = (predict_csv+predict_img)/2
    min = math.ceil(price)-10 if math.ceil(price)-10>=5 else 5
    max = math.ceil(price)+10
    price_range = str(min) + ' - ' + str(max)
    st.success(f"Suggested price: {price_range} $")
    st.image(img, use_column_width=True)

img = PILImage.create(fname)
predict(img, df)
