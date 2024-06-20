# Overview
The goal of this project is to create a ML infrastructure leveraging AWS sagemaker. This will be done using a student account thus limiting possible AWS services/features that will be used. The dataset for this problem is 
a [dataset](https://www.kaggle.com/datasets/adityadesai13/used-car-dataset-ford-and-mercedes?select=skoda.csv) about cars sale information. This dataset contains information such as car year, mileage, model, maker, etc and the goal 
will be to predict the price. 

### Code Structure
- [Data Processing](AwsDataProcessing.ipynb)
  - Data Processing
  - Data Uploading to S3
  - Base Model Training
  - Batch Transform
  - Base Model Uploading to sagemaker
- [Deploy](Deploy.ipynb)
  - Deploy sagemaker model endpoint
  - Create Monitor
  - Create CI/CD


---- 


Project Team Group #: 6


Authors:
- Aria Alaghemand
- Navid Aghaebrahim
- Nathan Edwards
