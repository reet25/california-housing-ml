# California Housing Price Prediction (Machine Learning Regression Project)

## Objective

The objective of this project is to predict California housing prices using multiple regression models and analyze their performance using evaluation metrics. The focus is on understanding model behavior, improving generalization, and studying the impact of preprocessing techniques such as outlier handling.

---

## Dataset

The project uses the **California Housing dataset**, which contains housing-related information from districts in California.

### Features include:
- Median Income  
- House Age  
- Average Rooms  
- Average Bedrooms  
- Population  
- Average Occupancy  
- Latitude  
- Longitude  

### Target:
- Median House Value  

---

## Workflow

This project follows a complete **end-to-end machine learning pipeline**:

### 1. Exploratory Data Analysis (EDA)
- Feature distribution analysis  
- Skewness detection  
- Correlation analysis  
- Outlier identification  

### 2. Data Preprocessing
- Train-test split  
- Outlier detection using IQR method  
- Selective outlier removal experiments  

### 3. Models Implemented
- Linear Regression (Baseline model)  
- Decision Tree Regressor  
- Random Forest Regressor  

### 4. Model Evaluation
- Mean Squared Error (MSE)  
- R² Score  
- Train vs Test performance comparison  

### 5. Model Validation
- K-Fold Cross Validation (5 folds)  

### 6. Model Optimization
- Hyperparameter tuning using RandomizedSearchCV  

### 7. Model Interpretation
- Residual analysis  
- Feature importance analysis (Random Forest)  

---

## Key Results

| Model | MSE | R² Score |
|------|------|----------|
| Linear Regression | ~0.5559 | ~0.5758 |
| Linear Regression (After Outliers Removed) | ~0.4095 | ~0.6844 |
| Decision Tree | ~0.50 | ~0.61 |
| Random Forest | ~0.2559 | ~0.8047 |
| Tuned Random Forest | ~0.2583 | ~0.8029 |

---

## Key Insights

- Random Forest performed best among all models  
- Linear Regression improved significantly after outlier handling  
- Decision Tree showed overfitting (high train score, lower test score)  
- Cross-validation gave more reliable performance estimates  
- Residual analysis showed limitations of linear models  
- Feature importance highlighted **Median Income** as the strongest predictor  

---

## Feature Importance (Random Forest)

Most important features:
- Median Income (strongest predictor)  
- AveOccup  
- Latitude / Longitude  

Less influential:
- Population  
- AveBedrms  

---

## Model Behavior Analysis

- Linear models struggled with non-linearity and outliers  
- Tree-based models captured complex relationships better  
- Random Forest balanced bias and variance effectively  
- Hyperparameter tuning improved stability but not drastically performance  

---

## Tech Stack

- Python  
- Pandas  
- NumPy  
- Scikit-learn  
- Matplotlib  

---

## Key Learnings

- End-to-end ML pipeline design  
- Impact of outliers on linear models  
- Model comparison techniques  
- Cross-validation for robust evaluation  
- Residual analysis for error diagnostics  
- Feature importance interpretation  
- Ensemble learning advantages  

---

## Future Improvements

- Try advanced models (XGBoost / LightGBM)  
- Feature engineering (log transforms, interactions)  
- Deployment using Streamlit or Flask  
- Expanded hyperparameter tuning  
