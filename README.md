# Network-Anomaly-Detection

Project Overview
This project focuses on developing a machine learning-based solution for detecting network anomalies in real-time, aimed at identifying unusual patterns in network traffic that could signify security threats. Traditional network security approaches rely on known signatures of attacks, but these methods can fall short when faced with evolving or previously unseen threats. This project takes a data-driven approach to tackle network anomaly detection, leveraging supervised and unsupervised learning techniques to detect potentially malicious activity.

Problem Statement
Network anomaly detection is crucial for identifying and mitigating cyber threats. The objective of this project is to design and deploy a model that can accurately classify network events as normal or anomalous, based on historical data of network activity. Anomalous behavior can be an early indicator of security threats such as DDoS attacks, compromised devices, and malware infections. The challenge lies in detecting these anomalies accurately, given the vast amount of noisy and heterogeneous network data.

Target Metric
The key metrics used to evaluate model performance are:

Accuracy: The overall correctness of predictions.
Precision and Recall: Especially relevant for imbalanced datasets to understand how well the model captures true anomalies while minimizing false positives.
F1 Score: Balances precision and recall, crucial for evaluating the model’s performance in detecting rare anomaly events.
For unsupervised methods, Anomaly Detection Rate and False Positive Rate are also monitored.

Project Workflow
Step 1: Exploratory Data Analysis (EDA)
Distribution Analysis: Key features like protocoltype, service, flag, and attack were examined for common values and distribution patterns.
Correlation Analysis: Identified high correlation features, such as srcbytes and dstbytes, to understand relationships between traffic flow volumes and anomalies.
Visualization: Histograms, box plots, and scatter plots helped identify patterns, such as high serrorrate in certain traffic and elevated srcbytes in attacks.
Step 2: Hypothesis Testing
Several hypotheses were tested to guide feature engineering:

Traffic Type Hypothesis: Traffic with unusual serrorrate and rerrorrate may indicate attacks (e.g., SYN floods).
Access Frequency Hypothesis: High values in count and srvcount indicate repeated access to services, potentially signaling probes or brute-force attempts.
Login Patterns: Features like numfailedlogins and isguestlogin were analyzed for anomalous login activity.
Step 3: Feature Engineering
Encoding Categorical Variables: Used OneHotEncoding and frequency encoding for protocoltype, service, and flag to retain categorical relationships.
Derived Features: Added session-level aggregates like total bytes transferred and calculated error rates for improved granularity in anomaly detection.
Step 4: Modeling
Logistic Regression served as a baseline model to provide initial insights.
Random Forest was employed for its ability to handle non-linear patterns in the data and yielded higher accuracy and robustness in detecting anomalies.
Step 5: Evaluation and Insights
Model Performance:
The Random Forest model achieved high accuracy and an F1 score, indicating a strong capability in distinguishing normal traffic from anomalies.

Insights and Recommendations
Traffic Patterns: The predominant protocols were TCP and HTTP. Frequent service access patterns indicate that more robust security for these protocols could reduce vulnerability.
Error Rates: High serrorrate and rerrorrate are strong indicators of potential anomalies, especially during DDoS or probe attacks.
User Behavior: Observations showed that accounts with frequent login failures are often flagged as anomalies, suggesting potential brute-force attacks.
Recommendations:
Enhanced Monitoring: Focus on high-risk protocols and services. Monitoring sessions with high serrorrate and rerrorrate could reduce false negatives.
Hybrid Model Approach: Combining unsupervised methods with supervised models can improve detection of new attack types.
Continuous Training: Retrain the model regularly to adapt to emerging attack patterns, ensuring it remains effective against evolving threats.
Deployment Steps
Model Saving: The trained Random Forest model and encoders (OneHotEncoder for categorical variables and LabelEncoder for labels) were saved as .pkl files.
Flask API: A Flask application was created to serve the model in real-time, accepting JSON input and returning predictions.
Environment Setup:
Created a requirements.txt file to handle dependencies.
Set up a virtual environment, installing Flask, scikit-learn, and other dependencies.
Testing: The API was tested using Postman and confirmed to accurately process input and return predictions.
Final Scores
Random Forest: The model achieved an F1 score of 1, with high precision and recall for anomaly detection.
Files in Repository
EDA and Modeling Notebook: Contains the code for EDA, hypothesis testing, feature engineering, and model training, with visualizations and insights.
Deployment Code: Flask API code and associated files for serving the model such as model files and ecsoding files and requirements file.

