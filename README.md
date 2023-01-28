### Car prediction Website link --> http://43.204.238.28/

# Predicting Car Prices Using Machine Learning with Deployment
This project is focused on using machine learning to predict the prices of used cars based on various features. The data for this project was scraped from an online car dealership website using Selenium. Once the data was collected, it was cleaned and preprocessed using Pandas in order to prepare it for training the machine learning model. Several machine learning algorithms were used to train the model, including Random Forest and Linear regression.

Once the model was trained, a Flask server was created to host the model. The server was also used to create dynamic HTML content that allows users to input their car information and receive a prediction of its price. This was then deployed on AWS platform. This allows users to easily access the model and receive accurate predictions without having to download and run the code locally.

<p align="center">
  <img src="Website Screenshot.jpg" width="500" height="500">
</p>

## Project Overview 
* Created an accurate model that can predict the prices of used car
* Enter your car details like brand name, model name, km ,etc in the web app and find out
* Predicts correctly with an 83% accuracy
* Collected the data, Cleaned the data and prepared the data for model training
* Optimized Naive bayes, Logistic regression, decision tree, random forest using ensembling methods to reach the best model.
* Finally a soft voting ramdom forest regressor achieved the best accuracy.

## Environment and tools
1. Scikit-learn
2. Selenium
3. Pandas
4. Numpy
5. Flask
6. AWS

## Installation

Download all the files above and save them in a folder. 
1. Install python.
2. Open CMD from the folder and type ``` pip install -r requirements.txt ```.
3. After Installation type ``` python app.py ```.
4. Click the link to access the site and predict car prices.

### Data Scraped from Carwala.com using Selenium library in python

