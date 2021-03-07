'''
MODULE KIRIM EMAIL MELALUI PYTHON
Referensi : https://gist.github.com/zita9999/8d7306c2d9312a5e974a466877b813c3
'''

#Importing Packages
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders

#Membuat List Email Penerima
file = open("receiver_list.txt", "r")
content = file.read()
content_list = content.split(" \n")
print(content_list)

#Pengirim dan Penerima
sender = 'achmad.ramdhany.irdiansyah@gmail.com'
receivers = content_list

#Isi Email
body_of_email = "Halo Semua. Ini adalah pesan otomatis yang dikirimkan dari Python. Aku lagi belajar Python lho guys"

#Membuat Pesan, SUbject Line, Penerima, dan Pengirim
msg = MIMEText(body_of_email, 'html')
msg['Subject'] = 'Email dari Phyton'
msg['From'] = sender
msg['To'] = ','.join(receivers)

#CMengubungan ke Server SMTP Gmail
s = smtplib.SMTP_SSL(host = 'smtp.gmail.com', port = 465)
s.login(user = sender, password = 'password')
s.sendmail(sender, receivers, msg.as_string())
s.quit()