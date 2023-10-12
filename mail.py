#!C:\Python311\python.exe
print("Content-Type:text/html\n\r")


import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb

db=MySQLdb.Connect(host="localhost",user="root",password="satheesh29",database="hcm")
cur=db.cursor()

import cgi
form=cgi.FieldStorage()
a=form.getvalue("em")
b=str(form.getvalue("ms1"))

cur.execute("SELECT * FROM pdt")
result = cur.fetchall()


from email.message import EmailMessage
import ssl
import smtplib
email_s='sksatheeshu29@gmail.com'
email_p='hryxjtanyuzeckmb'
email_r=a
subject="alert from HCM"
body=("hello,this is the message from HCM and  "+b)

em=EmailMessage()
em["From"]=email_s
em["To"]=email_r
em["Subject"]=subject
em.set_content(body)
context=ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context) as smtp:
    smtp.login(email_s,email_p)
    smtp.sendmail(email_s,email_r,em.as_string())
print('''<center>SUCCESSFULLY ALERT MAIL DELIVERD..</center>''')
