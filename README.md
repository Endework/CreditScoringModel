# Credit Scoring Model for Bati Bank

## Overview

Bati Bank, a leading financial institution, is developing a Credit Scoring Model to support a new "buy now, pay later" service in partnership with a growing eCommerce company. This service will allow customers to purchase products on credit, contingent upon their qualification.

## Objectives

1. **Risk Management**: Identify high-risk borrowers to minimize default risks.
2. **Customer Segmentation**: Tailor credit offerings and marketing strategies based on risk levels.
3. **Regulatory Compliance**: Adhere to Basel II Capital Accord requirements.
4. **Competitive Advantage**: Enhance Bati Bank's reputation and attract more customers.

## Process

1. **Data Collection**: Gather historical data of borrowers and their loan performance.
2. **Feature Selection**: Identify variables predicting default risk.
3. **Model Development**: Build models to assign risk probabilities and credit scores.
4. **Implementation**: Deploy the model for real-time credit risk assessment.

## Business Need

To implement the "buy now, pay later" service successfully, Bati Bank needs a robust Credit Scoring Model that addresses the following:

1. Accurate Risk Assessment
2. Enhanced Decision-Making
3. Operational Efficiency
4. Regulatory Adherence
5. Competitive Edge
6. Customer Personalization
7. Strategic Growth

## Understanding Credit Risk

Credit risk is the possibility of a borrower defaulting on their debt. Effective management involves:

1. **Traditional Models**: Analyze historical data to predict default likelihood.
2. **Alternative Approaches**: Use non-traditional data for a holistic view of creditworthiness.
3. **Basel II Accord**: Maintain capital reserves to cover potential losses.

## Developing a Credit Risk Model

Steps include data collection, feature selection, model building, validation, and continuous monitoring. Techniques like Weight of Evidence (WoE) and Information Value (IV) are used to assess feature predictive power.

## Data and Features

Data for this project includes transaction details like `TransactionId`, `AccountId`, `CustomerId`, `CurrencyCode`, `ProductCategory`, `Amount`, and `FraudResult`.

## Data Preparation and Feature Engineering

- **Data Visualization**: Analyzed the data distributions and outliers.
- **Feature Engineering**: Extracted features like `total_transaction_amount`, `average_transaction_amount`, `transaction_count`, and `stddev_transaction_amount`.
- **One-Hot Encoding**: Applied to non-numerical columns.
- **Normalization**: Used MinMaxScaler to normalize the numerical data.
- **RFM Features**: Extracted Recency, Frequency, and Monetary value features.

## Modeling

1. **Train-Test Split**: 80% training and 20% testing.
2. **Algorithms Tried**: Logistic Regression, K-Neighbors Classifier, Decision Tree Classifier, Random Forest Classifier, Support Vector Classifier, and XGBoost Classifier.
3. **Best Model**: XGBoost Classifier was identified as the best-performing model.

## Model Deployment

1. **FastAPI Application**: Created to serve the model predictions.
2. **Ngrok**: Used to expose the local FastAPI server to the internet for testing.

## Project Accomplishments

In this project, I planned to perform extensive data visualization and further analyze the dataset, and I successfully accomplished those goals. Additionally, I deployed the model as an API. Moving forward, I plan to explore more algorithms to train the data and create an even better model. I also aim to improve the Flask app's UI/UX to make it more appealing and user-friendly.

## Getting Started

### Prerequisites

- Python 3.7+
- FastAPI
- Uvicorn
- Pyngrok
- XGBoost
- Joblib
- Pandas

### Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/Endework/CreditScoringModel.git
    cd CreditScoringModel
    ```

2. **Install required packages**:
    ```sh
    pip install fastapi uvicorn pyngrok xgboost joblib pandas
    ```

3. **Download and prepare the data**:
    Ensure you have the dataset named `predata.csv` in the project directory.



## References

- [Colabcode: Deploying Machine Learning Models from Google Colab](https://towardsdatascience.com/colabcode-deploying-machine-learning-models-from-google-colab-54e0d37a7b09)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Ngrok Documentation](https://ngrok.com/docs)

## Future Work

In this project, I planned to perform extensive data visualization and further analyze the dataset, and I successfully accomplished those goals. Additionally, I deployed the model as an API. Moving forward, I plan to explore more algorithms to train the data and create an even better model. I also aim to improve the Flask app's UI/UX to make it more appealing and user-friendly.

## License

This project is licensed under the MIT License.
