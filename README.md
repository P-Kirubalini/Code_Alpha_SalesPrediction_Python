# Sales Prediction Using Python

## Project Overview
This project predicts future sales based on advertising spend, platform used, and target customer segment.
It uses a Linear Regression model to analyze how marketing factors impact sales and helps businesses
make better marketing decisions.

## Objectives
- Predict future sales using advertising data
- Analyze the impact of advertising spend on sales
- Understand platform and target segment influence
- Provide insights for marketing strategy improvement

## Technologies Used
- Python
- Pandas
- Scikit-learn
- Linear Regression

## Dataset Description
The dataset contains the following columns:
- Advertising_Spend: Amount spent on advertisements
- Platform: Marketing platform (Instagram, Facebook, Google)
- Target_Segment: Customer segment (Youth, Adults)
- Sales: Sales value (target variable)

## Data Preprocessing
- Converted categorical variables into numerical format using one-hot encoding
- Selected relevant features
- Split data into training and testing sets

## Model Used
Linear Regression is used to predict sales based on advertising and marketing factors.

## Model Evaluation
The model performance is evaluated using:
- Mean Squared Error (MSE)
- R2 Score

## Future Sales Prediction
The trained model predicts sales for new advertising data such as increased ad spend,
specific platform, and target segment.

## Key Insights
- Higher advertising spend leads to higher sales
- Some platforms perform better than others
- Target customer segment affects sales outcome

## How to Run
1. Install required libraries:
   pip install pandas scikit-learn
2. Run the Python file:
   python sales_prediction.py

## Conclusion
This project shows how machine learning can be used to forecast sales and support
data-driven marketing strategies.
