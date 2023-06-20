# Load/Performance-Testing-For-ML-Applications
Performance Testing is a type of software testing which ensures that the application is performing well under the workload. The goal of performance testing is not to find bugs but to eliminate performance bottlenecks. It measures the quality attributes of the system. 

Stepwise Procedure to carry out load testing for your Machine Learning Models deployed at GCP Vertex AI Endpoint. (One could also use this code for AWS Sagemaker Endpoint)
1. Open VS Code and its terminal.
2. Install locust by using "pip install locust"
3. Get G_Token by using below commands:
   a. Log in into your GCP Project account by using command in VS Code terminal: "gcloud auth login"
   b. Print access token using the command: "gcloud auth print-access-token"
   c. Copy the access token and paste in locustfile.py file (Line 7)
4. Set Endpoint_ID, PROJECT_ID, REGION in line no 10, 11 and 12.(locustfile.py)
5. In headers of locustfile.py select the content type that you are going to provide as input to model. Generally google vertex ai needs the model input in json format.
6. No need to change the code from line no.19 onwards in locustfile.py file
7. Create the seperate input_json.json file which contains Model Request in json format. This is input that we need to provide to the model and model will give us prediction. Make sure you given the valid request that will give us 200 response code.
8. Use the command to run the load test:  "locust -f locustfile.py"
9. Once test started, you need to paste this url in your local chrome browser: "http://localhost:8089/"
10. The above step will open locust ui. You will see the following window. Fill it with necessary information and start sawarming.
    ![image](https://github.com/rajeshmore1/Load-Performance-Testing-For-ML-Applications/assets/73220561/73da68e6-9105-43ba-8208-3890e77ea666)
    
a. Total number of users: Number of users that are going to use you ML Applications. Lets say 10.

b. Spawn Rate: spawn rate of 0.1 means number of users started per second. Starting from 1 user, we will increase the users by 0.1 per seconds. All 10 users are not simultaneously using our API endpoint.

3. Host: If you have deployed your model at us-central1 location. the host would be "https://us-central1-aiplatform.googleapis.com".
4. 
11. Once you fill above information you can see the metrics in locust ui like - Request Statistics, Response Time Statistics, Charts such as Total Request Per Second, Response Times (ms), Number of USers. One can download the report in csv format or html format and decide the most suitable machine type for your Machine Learning Application like n1-standard-2, number of accelerators, accelerator type, autoscaling metrics specifications etc.
    
![image](https://github.com/rajeshmore1/Load-Performance-Testing-For-ML-Applications/assets/73220561/7db44a73-881c-4d12-b923-55dd0029ab8e)


Usefull Articles: 
1. Performance Testing on GCP: https://cloud.google.com/ai-platform/prediction/docs/load-testing-and-monitoring-aiplatform-models
2. Sayakpaul's repo: https://github.com/sayakpaul/deploy-hf-tf-vision-models/tree/main/hf_vision_model_vertex_ai
