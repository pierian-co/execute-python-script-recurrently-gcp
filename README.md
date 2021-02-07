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
[Step 1: Create a project in GCP](#step1)

[Step 2: Prepare local environmant for GCP actions](#step2)

[Step 3: Setup Python locally](#step3)

[Step 4: etup Gmail account to send emails using SMTP](#step4)

[Ste 5: Send test email](#step5)

[Step 6: Enable Google Clound Function and Cloud Scheduler on your project](#step6)


## Steps in detail

### <a name="step1"></a>Step 1: Create a project in GCP

1. Login to Google Cloud Console and [create a new project](https://console.developers.google.com/projectcreate) 

2. Name the project. 

### <a name="step2"></a>Step 2: Setup local environment for GCP actions

1. Download GCP SDK from https://cloud.google.com/sdk/docs/install

2. Open command line and initialise GCP SDK using command gcloud init

3. Select Create a new configuration and provide a name

4. Choose the account. It may ask you for login into GCP account. Read more about [GCP Authorizing](https://cloud.google.com/sdk/docs/authorizing)

5. Select the number corresponding to the project created in Step 1. 

### <a name="step3"></a>Step 3: Setup Python locally

1. Follow steps at https://cloud.google.com/python/docs/setup to isntall Python

2. Create a Virtual Environment to isolate dependencies using the steps in above URL. This should create a new directory *env* in your project-folder. 

### <a name="step4"></a>Step 4: Setup Gmail account to send emails using SMTP

For security reasons, Gmail doesnt allow emails to be sent programmatically until you enable *less secure apps* to do so.

1.  Visit https://www.google.com/settings/security/lesssecureapps after logging in to your Gmail account you want to use for sending emails.

### <a name="step5"></a>Step 5: Send test email

1. Download the main.py file from this project. Provide the gmail-account, password and recipient email address in the script.

2. Run the script by typing `python main.py`

3. Check your Gmail account. If you have recieved an email with subject *Security Alert* then click on it and selct the option *Accpet it was you*.

4. Run the script again and check the recpient-email account to confirm test email is recieved. 

### <a name="step6"></a> Step 6: Enable googlecoundfunction API on the project

https://console.developers.google.com/apis/api/cloudbuild.googleapis.com/overview?project=454733612595

Ste 6: Enable cloudscheduler.googleapis.com 

gcloud functions deploy my_function --entry-point main --runtime python37 --trigger-resource my_topic --trigger-event google.pubsub.topic.publish --timeout 540s

gcloud scheduler jobs create pubsub my_job2 --schedule "*/2 * * * *" --topic my_topic --message-body "message_body"

