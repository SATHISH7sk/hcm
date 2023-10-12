import smtplib
email="satheeshkumarsk@gmail.com"
x="hryxjtanyuzeckmb"
password=x
subject="xxxxx"
msg="yyyy"
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(email,password)
to_email="sksatheeshu29@gmail.com"
body='\r\n'.join(['To: %s' % to_email,'From: %s' % email,'Subject: %s' %subject,'',msg])
server.sendmail(email,to_email,body)
