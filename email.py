import smtplib


sender = "joyaljoykarunagappally@gmail.com"
receiver = "joyaljoy514@gmail.com"
password = "/j1(o2y3a4)l5/14"
subject = "python email test"
body = "hello world"

message = f"""From: {sender}
To: {receiver}
subject: {subject}\n
{body}
"""

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

server.login(sender, password)
print("log in...")
server.sendmail(sender, receiver, message)
print("sent success")