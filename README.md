# California Housing Price Prediction  
### Machine Learning Regression & Deployment Project

## Project Overview

This project focuses on predicting California housing prices using multiple machine learning regression models and evaluating their performance using standard regression metrics.

The project demonstrates a complete end-to-end machine learning workflow including:

- Exploratory Data Analysis (EDA)
- Data preprocessing
- Outlier handling
- Model training & comparison
- Cross-validation
- Hyperparameter tuning
- Residual analysis
- Feature importance interpretation
- Streamlit deployment

A deployed Streamlit application was also created to generate real-time housing price predictions using the trained model.

---

# Objective

The objective of this project is to analyze housing-related data from California districts and build regression models capable of predicting median house values accurately while understanding model behavior, generalization, and preprocessing impact.

---

# Dataset Information

The project uses the **California Housing Dataset** available through Scikit-learn.

### Dataset Size
- 20,640 samples
- 8 numerical input features

### Features Used
- Median Income
- House Age
- Average Rooms
- Average Bedrooms
- Population
- Average Occupancy
- Latitude
- Longitude

### Target Variable
- Median House Value

---

# Project Workflow

## 1. Exploratory Data Analysis (EDA)

Performed:
- Distribution analysis
- Correlation analysis
- Skewness detection
- Outlier identification
- Feature relationship analysis

---

## 2. Data Preprocessing

Implemented:
- Train-test split
- Outlier detection using IQR method
- Selective outlier removal
- Data cleaning experiments

---

## 3. Machine Learning Models Used

### Linear Regression
Used as a baseline regression model.

### Decision Tree Regressor
Used to capture non-linear relationships in housing data.

### Random Forest Regressor
Used ensemble learning to improve prediction accuracy and reduce overfitting.

---

# Model Evaluation

Models were evaluated using:

- Mean Squared Error (MSE)
- R² Score
- Train vs Test comparison
- Cross-validation performance

---

# Model Validation

Implemented:
- K-Fold Cross Validation (5 folds)

This provided more reliable estimates of model generalization compared to a single train-test split.

---

# Hyperparameter Tuning

Applied:
- `RandomizedSearchCV`

Used to optimize:
- Number of estimators
- Maximum depth
- Minimum samples split

---

# Residual Analysis

Residual analysis was performed to:
- Evaluate model error patterns
- Detect heteroscedasticity
- Analyze prediction limitations of linear models

---

# Feature Importance Analysis

Feature importance analysis using Random Forest revealed:

### Most Important Features
- Median Income
- Average Occupancy
- Latitude / Longitude

### Less Influential Features
- Population
- Average Bedrooms

---

# Model Performance

| Model | MSE | R² Score |
|------|------|------|
| Linear Regression | ~0.5559 | ~0.5758 |
| Linear Regression (After Outlier Removal) | ~0.4095 | ~0.6844 |
| Decision Tree Regressor | ~0.50 | ~0.61 |
| Random Forest Regressor | ~0.2559 | ~0.8047 |
| Tuned Random Forest | ~0.2583 | ~0.8029 |

---

# Key Insights

- Random Forest achieved the best overall performance.
- Linear Regression improved significantly after outlier handling.
- Decision Trees showed overfitting tendencies.
- Ensemble learning improved model generalization.
- Cross-validation provided more stable evaluation results.
- Feature importance analysis highlighted Median Income as the strongest predictor.

---

# Streamlit Deployment

A Streamlit web application was developed to allow users to generate real-time housing price predictions interactively.

## Deployment Features
- Interactive input fields
- Real-time predictions
- Trained model loading using Joblib
- Simple ML deployment workflow

---

# Tech Stack

## Programming & ML
- Python
- Pandas
- NumPy
- Scikit-learn

## Visualization
- Matplotlib

## Deployment
- Streamlit
- Joblib

---

# Key Learnings

Through this project, I strengthened my understanding of:

- End-to-end ML pipeline development
- Regression modeling
- Outlier handling techniques
- Model comparison
- Cross-validation
- Hyperparameter tuning
- Residual diagnostics
- Feature importance interpretation
- Ensemble learning
- Basic ML deployment using Streamlit

---

# Project Structure

```bash
california-housing-ml/
│
├── California_Housing_Price_Prediction.ipynb
├── app.py
├── random_forest_model.pkl
├── requirements.txt
└── README.md
```

---

# Future Improvements

Potential future improvements include:

- XGBoost / LightGBM implementation
- Advanced feature engineering
- Improved hyperparameter tuning
- Better UI customization
- Permanent cloud deployment

