# AI-Driven Customer Analytics Platform

## Developed By

**MOHAMMAD MASTAN VALI SHAIK**

---

## Project Overview

The AI-Driven Customer Analytics Platform is a machine learning-based web application developed using Python and Streamlit. The platform helps businesses understand customer behavior, identify valuable customer segments, predict purchasing likelihood, analyze customer churn risk, and generate business reports for decision-making.

The system combines customer segmentation, predictive analytics, data visualization, and reporting into a single interactive dashboard.

---

## Objectives

* Analyze customer behavior using data analytics
* Segment customers using Machine Learning
* Predict purchase likelihood
* Analyze customer churn risk
* Generate business reports
* Support data-driven marketing decisions

---

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* Plotly
* Streamlit
* Pickle
* ReportLab

---

## Machine Learning Algorithms

### K-Means Clustering

Used to segment customers into different groups based on:

* Annual Income
* Spending Score

### Random Forest Classifier

Used to predict customer purchase likelihood based on:

* Age
* Annual Income
* Spending Score
* Gender

### Rule-Based Churn Analysis

Used to identify customers who may leave the business based on:

* Spending behavior
* Income level
* Age

---

## Project Features

### Dashboard

* Customer KPIs
* Customer Search
* Cluster Filtering
* Download Customer Data
* Customer Segmentation Visualization
* Business Insight Graphs
* Cluster Summary
* High Value Customer Identification

### Purchase Prediction

* Purchase Probability Prediction
* Customer Profile Analysis
* Marketing Recommendations

### Churn Analysis

* Churn Risk Assessment
* Risk Categorization
* Retention Recommendations

### Marketing Recommendations

* Segment-Based Marketing Strategies
* Customer Engagement Suggestions

### Report Generation

* PDF Report Export
* CSV Report Export

---

## Project Structure

AI_Customer_Analytics/

│

├── data/

│ ├── customers.csv

│ └── customers_clustered.csv

│

├── models/

│ └── purchase_model.pkl

│

├── pages/

│ ├── dashboard.py

│ ├── prediction.py

│ ├── churn.py

│ ├── recommendations.py

│ └── report.py

│

├── utils/

│ ├── helpers.py

│ └── preprocessing.py

│

├── app.py

├── train_model.py

├── generate_dataset.py

├── requirements.txt

└── README.md

---

## Installation

Install all required libraries:

```bash
pip install -r requirements.txt
```

---

## Running the Project

### Step 1

Generate Dataset

```bash
python generate_dataset.py
```

### Step 2

Train Machine Learning Model

```bash
python train_model.py
```

### Step 3

Run Streamlit Application

```bash
streamlit run app.py
```

---

## Business Benefits

* Customer Segmentation
* Customer Behavior Analysis
* Purchase Prediction
* Churn Analysis
* Marketing Optimization
* Better Customer Retention
* Data-Driven Decision Making

---

## Future Enhancements

* Real-Time Database Integration
* Customer Lifetime Value Prediction
* Advanced Churn Prediction Models
* Email Campaign Integration
* Automated Marketing Recommendations

---

## Author

**MOHAMMAD MASTAN VALI SHAIK**

B.Tech Student

AI-Driven Customer Analytics Platform

Academic Project
