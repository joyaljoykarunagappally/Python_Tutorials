import smtplib
def send_email(sender, receiver, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login('joyaljoy514@gmail.com', '/j1(o2y3a4)l5/14')
    server.sendmail(sender, receiver, message)
    server.quit()

subject = "My Subject"
body = "My message"
sender = "sender@gmail.com"
receiver = "receiver@gmail.com"

send_email(sender, receiver, body)