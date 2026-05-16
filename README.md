# California Housing Price Prediction using Machine Learning

## Project Overview
This project focuses on predicting California housing prices using machine learning regression models. The goal is to analyze housing data, build predictive models, compare their performance, and understand how preprocessing techniques like outlier removal affect model accuracy.

The dataset used is the **California Housing dataset**, which contains information about housing districts in California including income levels, number of rooms, population, and geographical data.

---

## Objective
- Predict median house values in California districts
- Compare multiple regression models
- Analyze model performance using evaluation metrics
- Study impact of preprocessing and outlier handling

---

## Dataset Information
The dataset contains 20,640 samples with 8 numerical features:

- MedInc (Median Income)
- HouseAge
- AveRooms
- AveBedrms
- Population
- AveOccup
- Latitude
- Longitude

Target variable: Median House Value

---

## Machine Learning Models Used

- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor

---

## Evaluation Metrics

- Mean Squared Error (MSE)
- R² Score
- Train vs Test Score Comparison

---

## Model Performance Comparison

| Model | MSE | R² Score | Train Score | Test Score |
|------|------|----------|-------------|------------|
| Linear Regression | 0.5559 | 0.5758 | 0.6126 | 0.5758 |
| Linear Regression (After Outlier Removal) | 0.4095 | 0.6844 | 0.6421 | 0.6844 |
| Decision Tree Regressor | 0.5016 | 0.6172 | 1.0000 | 0.6172 |
| Random Forest Regressor | 0.2559 | 0.8047 | 0.9735 | 0.8047 |

---

## Key Insights

- Linear Regression improved significantly after outlier removal, showing sensitivity to extreme values.
- Decision Tree Regressor overfitted the training data (perfect training score).
- Random Forest Regressor performed the best overall due to ensemble learning and better generalization.
- Not all outliers should be removed; some contain meaningful predictive information.

---

## Data Preprocessing Techniques

- Train-test split (80/20)
- Outlier detection using IQR method
- Selective outlier removal
- Exploratory Data Analysis (EDA)

---

## Conclusion

This project demonstrates that:
- Model performance depends heavily on data quality
- Simple models can improve significantly with preprocessing
- Ensemble methods like Random Forest provide the best balance of accuracy and generalization

Random Forest was the best-performing model for this dataset.

---

## Future Improvements

- Hyperparameter tuning
- Feature engineering (e.g., interaction features)
- Cross-validation
- Deployment using Flask or Streamlit
