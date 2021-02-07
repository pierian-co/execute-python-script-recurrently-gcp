import smtplib

# Gmail-account details to send email from
gmail_user = "your-account@gmail.com"  
gmail_password = "password"

# Email address of recipient
send_to = "receipient email address"

def main(data, context):
    try:  
        # creates SMTP session 
        session = smtplib.SMTP('smtp.gmail.com', 587) 

        # start TLS for security 
        session.starttls()

        # Authenticate with Gmail-account
        session.login(gmail_user, gmail_password) 

        # message body
        message = "This is a test email sent by " + gmail_user

        # send the mail 
        session.sendmail(gmail_user, send_to, message) 

        # terminate the session 
        session.quit() 

        print ("Email sent successfully")
    except:  
        print('Something went wrong...')

if __name__ == "__main__":
    main('data','context')
    