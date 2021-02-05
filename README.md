# Executing Python script recurringly using Google Cloud

Many times we want our Python code to be executed repeatedly after specific interval to meet business goals. Some examples:
1. Read data from an offline source every mid-night and update your business reports
2. Vaidate the data for PII every hour
3. Send emails to a user-list to remind 

Step 1: Download GCP SDK: https://cloud.google.com/sdk/docs/install 

Step 2: Select your current project

Step 3: https://cloud.google.com/sdk/docs/authorizing

Step 4: Setup Python locally: https://cloud.google.com/python/docs/setup

Step 5: Enable googlecoundfunction API on the project

https://console.developers.google.com/apis/api/cloudbuild.googleapis.com/overview?project=454733612595

Ste 6: Enable cloudscheduler.googleapis.com 
