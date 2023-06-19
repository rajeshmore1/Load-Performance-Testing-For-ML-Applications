from locust import HttpUser, task
import json
import os

# G_TOKEN = os.environ.get('G_TOKEN')

G_TOKEN="ya29.a0AWY7CklfGTJ7ZKEks6EvMXcXrDyGcdGV_lrryjX_F-9o2GzWTnj9FQvzJphY9n7jeilueSTImidt1LJoaCgYKAWoSARESFQG1tDrpbL6aAQt02-8_EONGlNaMgA0171"

class PredictModel(HttpUser):
    ENDPOINT_ID="5268749769139811111"
    PROJECT_ID="353405444111"
    REGION = "us-central1"
    headers = {
        'Content-Type': 'application/json',
        'Accept':'application/json',
        "Authorization": f"Bearer {G_TOKEN}"
        }

    @task
    def predict(self):
        ENDPOINT = f"/v1/projects/{self.PROJECT_ID}/locations/{self.REGION}/endpoints/{self.ENDPOINT_ID}:predict"
        instance = ""
        with open('./input_json.json') as f:
            instance = json.load(f)
        response = self.client.post(ENDPOINT, json=instance, headers=self.headers)
        print(f"Response: status_code: {response.status_code}")
        print(f"Response: response_data: {response.json()}")
