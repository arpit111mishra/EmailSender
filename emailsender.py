import smtplib
to = input("Enter the content of recipent:\n")
content=input("Enter the content:\n ")
def sendEmail(to,content):
    server= smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('senderemail@gmail.com','1233')
    server.sendmail('senderemail@gmail.com',to,content)
    server.close()
sendEmail(to,content)    