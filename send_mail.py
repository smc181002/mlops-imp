import smtplib, ssl, os
acc = ""

with open('command.txt', 'r') as file:
    acc = file.read()

#Next, log in to the server
userEmail = os.environ.get('EMAIL_USER')
password = os.environ.get('EMAIL_PASS')
senderEmail = 'meherchaitanya18802@gmail.com'
with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login(userEmail, password)

    subject = "your ML model report"
    body = "your model is trained with accuray: {0}".format(acc)
    msg = "Subject: {0}\n\n{1}".format(subject, body)

    smtp.sendmail(userEmail, senderEmail, msg)
