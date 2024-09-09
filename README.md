# Anime Commission Suggested Price
[![Static Badge](https://img.shields.io/badge/Medium%20article-black?style=for-the-badge&logo=medium)](https://medium.com/@pradrattana/%E0%B9%81%E0%B8%99%E0%B8%B0%E0%B8%99%E0%B8%B3%E0%B8%A3%E0%B8%B2%E0%B8%84%E0%B8%B2%E0%B8%A3%E0%B8%B9%E0%B8%9B%E0%B8%84%E0%B8%AD%E0%B8%A1%E0%B8%A1%E0%B8%B4%E0%B8%8A%E0%B8%8A%E0%B8%B1%E0%B8%99%E0%B8%AD%E0%B8%99%E0%B8%B4%E0%B9%80%E0%B8%A1%E0%B8%B0%E0%B8%94%E0%B9%89%E0%B8%A7%E0%B8%A2-fastai-ml-975ef50f1004)

Addressing the underpricing of anime commission art, this repository presents a machine learning model and a web application that provides suggested prices. This is my capstone project for AI Builders, aiming to empower artists to set fair prices for their work.

## Data Collection
Web scraping techniques were employed to extract data from [artistsnclients.com](https://artistsnclients.com/) (2021). Detailed scripts for this process are available in the [artistsnclients-scraping repository](https://github.com/pradrattana/artistsnclients-scraping.git).

## Machine Learning Model
My machine learning model averages the predictions of two sub-models:
1. **Image Regression Model**: This model uses only images for price prediction. Image scaling and data augmentation are added to ensure the model can learn from images with different views.
2. **Tabular Regression Model**: Recognizing that commission pricing is influenced by various factors beyond visual aesthetics, this model incorporates additional data stored in a tabular format.

For more details, please refer to this training notebook: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/pradrattana/anime_commission_suggested_price/blob/main/anime_price_reg.ipynb)

## Web Application
To make the model accessible for real-world use, a Streamlit web app is deployed on Heroku's free tier. This web app offers flexibility - you can choose to use only the image regression model for price suggestions.

Here is the web application: [![Static Badge](https://img.shields.io/badge/Open%20in%20Heroku-white?style=flat&logo=heroku&color=%23543c75)](https://anime-commission-price-14e7f45d1a2c.herokuapp.com/)
