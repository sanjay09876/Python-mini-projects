import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.login("youremailusername", "password")
msg = "Hello!" 
server.sendmail("you@gmail.com", "target@example.com", msg)
server.close()

