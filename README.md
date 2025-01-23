# faang__mlflow_project
## Problem Statement
To develop an intelligent and user-friendly Streamlit web application that predicts the closing price of FAANG stocks based on user inputs.
The tool should empower financial analysts and retail investors by simplifying complex data-driven decisions, providing them with accurate regression-based predictions of stock prices.
## Data Cleaning
Data cleaning  is the process of identifying, correcting, and handling errors, inconsistencies, and inaccuracies in a dataset to improve its quality and usability. It involves removing or fixing issues such as:
Missing data ,Duplicate entries ,Inconsistent formatting ,Outliers and Incorrect data.
## Remove outliers 
Removing outliers is an important step in data cleaning to ensure that extreme or anomalous values do not distort the analysis or model outcomes. 
In my dataset to identify outliers in price and volume columns using,
IQR (Interquartile Range): Remove or clip the data points outside the acceptable range.
Z-Score: Filter values with z-scores greater than 3 or less than -3.
## Descriptive Statistics
Descriptive statistics summarize the key characteristics of numerical columns in your dataset, offering insights into their central tendency, variability, and range. Common metrics include:

Mean: The average value.

Median: The middle value when data is sorted.

Mode: The most frequently occurring value.

Minimum and Maximum: The smallest and largest values in the dataset.

Standard Deviation: A measure of the spread or dispersion of values around the mean.
## Data Visualization
Visualizations help make complex data more accessible and understandable. The recommended visualizations are:

### Line Charts
Show trends over time, such as stock price movements or volume changes.
### Correlation Heatmaps
Display the pairwise correlation between features to identify relationships (positive or negative).
### Box Plots
Summarize the distribution of data and detect outliers.
### Scatter Plots
Visualize relationships between two continuous variables, such as stock prices and trading volume.
## Feature Selection 
Feature Selection narrows down relevant predictors, improving the efficiency and accuracy of models.
## Model Development
### Train-Test Split
Splitting the dataset is a critical first step to evaluate the model's performance on unseen data.
80% Training, 20% Testing: A common split ratio where the training set is used to train the model, and the testing set evaluates its performance.
## Model Selection
Begin with regression models to predict continuous variables (e.g., stock prices). Common choices include:

### Linear Regression:
Simple, interpretable, and works well for linearly correlated features.
### Decision Trees:
Non-linear model that splits data into hierarchical decision rules.
### Random Forest Regressors:
Ensemble method that combines multiple decision trees for robust predictions.
### Gradient Boosting Models:
Advanced ensemble methods like XGBoost or LightGBM provide high performance by correcting errors iteratively.
## Model Training
Once a model is selected, train it on the training dataset:
Use Cross-Validation (e.g., K-Fold):
Splits the training set into multiple subsets to evaluate the model's consistency across different folds.
Reduces the risk of overfitting and ensures robust performance.
## Hyperparameter Tuning
Optimize the model's performance by fine-tuning its parameters.
I used Grid Search, its Exhaustively searches a predefined parameter grid for the best combination.
## Purpose of MLflow Integration
Experiment Tracking: Keep a detailed record of experiments, including metrics, parameters, and artifacts.
Model Comparison: Quickly compare and evaluate models to choose the best-performing one.
Efficient Deployment: Simplify the transition of models from development to production.
MLflow ensures a streamlined and reproducible workflow, making it easier to manage the end-to-end lifecycle of machine learning projects.
## Deployment with Streamlit
A machine learning model using Streamlit, a lightweight and interactive framework for building data-driven web applications.
The focus here is on creating a user-friendly app for stock price prediction using a pre-trained model saved with MLflow.
In that streamlit interface the interactive user inputs for stock details or forecast parameters.
To know the dynamic predictions and visualizations and a clean and accessible interface for non-technical users.
