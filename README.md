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

[Step 4: Setup Gmail account to send emails using SMTP](#step4)

[Step 5: Send test email](#step5)

[Step 6: Enable required Google Clound APIs on your project](#step6)

[Step 7: Schedule Python script using Cloud Function and Pub-Sub(#step7)


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

> In case your script has dependencies on packages that are needed to be installed using pip, create a *requirements.txt* and add all those these (separated by enter)

### <a name="step6"></a> Step 6: Enable required GCP APIs on the project

1. in GCP, select the project created in [Step 1](#step1).

2. Enable [Cloud Build API](https://console.developers.google.com/apis/api/cloudbuild.googleapis.com/overview)

3. Enable [Cloud Scheduler API](https://console.developers.google.com/apis/api/cloudscheduler.googleapis.com/overview)

4. Enable [App Engine Admin API](https://console.developers.google.com/apis/api/appengine.googleapis.com/overview)


### <a name="step7"></a> Step 7: Schedule Python script

1. Deploy your Python script uisng GCP Cloud Functions using following command on the commandline

`gcloud functions deploy NAME-OF-YOUR-FUNCTION --entry-point main --runtime python37 --trigger-resource NAME-OF-TOPIC --trigger-event google.pubsub.topic.publish --timeout 540s`

Example:

`gcloud functions deploy my_function --entry-point main --runtime python37 --trigger-resource my_topic --trigger-event google.pubsub.topic.publish --timeout 540s`

2. Create a scheduled job using Cloud Scheduler:

`gcloud scheduler jobs create pubsub JOB-NAME --schedule "UNIX-STYLE-SCHEDULE-FREQUENCY" --topic NAME-OF-TOPIC --message-body "message_body"`

Here's an example of for scheduling jon every one minute:

`gcloud scheduler jobs create pubsub my_job2 --schedule "*/1 * * * *" --topic my_topic --message-body "message_body"`

3. If prompted to create an App Engine, do so by pressing *Y* and selecting appropriate location for your App Engine.

### <a name="step8"></a> Step 8: Validate its working

Check the recipient email account to confirm emails are being recieved.

> Once you have tested successfully, highly recommend to turn off *less secure apps* by visiting https://www.google.com/settings/security/lesssecureapps. 




