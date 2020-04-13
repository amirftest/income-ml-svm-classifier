# A function that sends the email of the result to hadas.c@velismedia.com.
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from status import *

email_status = Status.UNINITIALIZED

def sendemail(result):
    global email_status
    sender_address = 'amirftestclassifier@gmail.com'
    sender_pass = 'testclassifier'
    receiver_address = "hadas.c@velismedia.com"
    mail_content = f"Hey VelisMedia,\n\nThe Error Percentage is {result}.\n\nBest Regards,\nAmir."
    if email_status == Status.UNINITIALIZED:
        email_status == Status.IN_PROGRESS
        try:
            email_status = Status.IN_PROGRESS
            message = MIMEMultipart()
            message['From'] = sender_address
            message['To'] = receiver_address
            message['Subject'] = 'Amir Friedman | Home Assignment'
            message.attach(MIMEText(mail_content, 'plain'))
            session = smtplib.SMTP('smtp.gmail.com', 587)
            session.ehlo()
            session.starttls()
            session.login(sender_address, sender_pass)
            text = message.as_string()
            session.sendmail(sender_address, receiver_address, text)
            session.quit()
            email_status = Status.UNINITIALIZED
            return Status.DONE
        except Exception as e:
            print(e)
            return -1
    else:
        return email_status





