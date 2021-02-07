# Executing Python script recurringly using Google Cloud

Many times we want our Python code to be executed repeatedly after specific interval to meet business goals. Some examples:
1. Read data from an offline source every mid-night and update your business reports
2. Vaidate the data for PII every hour
3. Send emails to a user-list to remind

In this exerercse, we'll sending an email from a Gmail account every minute, using Google Cloud.

## Prerequisites:
1. Access to Google Cloud and its components: Cloud Function, Cloud Scheduler and Pub-Sub
2. Python 3
3. A Gmail account that can be used to send emails, and another email account to recieve emails

## Steps Summary
Step 1: Create a project in GCP

Step 2: Prepare local environmant for GCP actions

Step 3: Setup Python locally

Step 4: Enable Google Clound Function and Cloud Scheduler on your project

Ste 5: Setup Gmail account to send emails using SMTP

Step 6: Setup Python code to execute recurringly

## Steps in detail

### Step 1: Create a project in GCP

Login to ![Google Cloud] (https://console.developers.google.com/)  and create a new project


Download GCP SDK: https://cloud.google.com/sdk/docs/install 

Step 2: Select your current project

Step 3: https://cloud.google.com/sdk/docs/authorizing

Step 4: Setup Python locally: https://cloud.google.com/python/docs/setup

Step 5: Enable googlecoundfunction API on the project

https://console.developers.google.com/apis/api/cloudbuild.googleapis.com/overview?project=454733612595

Ste 6: Enable cloudscheduler.googleapis.com 

gcloud functions deploy my_function --entry-point main --runtime python37 --trigger-resource my_topic --trigger-event google.pubsub.topic.publish --timeout 540s

gcloud scheduler jobs create pubsub my_job2 --schedule "*/2 * * * *" --topic my_topic --message-body "message_body"

