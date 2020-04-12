# A function that sends the email of the result to hadas.c@velismedia.com.
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from tkinter import messagebox

def sendemail(result):

    sender_address = 'amirftestclassifier@gmail.com'
    sender_pass = 'testclassifier'
    receiver_address = "amirf2@gmail.com"
    mail_content = f"Hey VelisMedia,\nThe Error Percentage is {result}.\nThank You"
    try:
        message = MIMEMultipart()
        message['From'] = sender_address
        message['To'] = receiver_address
        message['Subject'] = 'Finished The Program'
        message.attach(MIMEText(mail_content, 'plain'))
        session = smtplib.SMTP('smtp.gmail.com', 587)
        session.ehlo()
        session.starttls()
        session.login(sender_address, sender_pass)
        text = message.as_string()
        session.sendmail(sender_address, receiver_address, text)
        session.quit()
        messagebox.showinfo("Success", "email was sent successfully!")
    except Exception as e:
        messagebox.showerror("Error", e)





