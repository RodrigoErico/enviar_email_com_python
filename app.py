import os
import smtplib
from email.message import EmailMessage
from secret import password

EMAIL_ADDRESS = 'remetente@gmail.com'
EMAIL_PASSWORD = password

msg = EmailMessage()
msg['Subject'] = 'Aqui será o assunto da mensagem!'
msg['From'] = 'remetente@gmail.com'
msg['To'] = 'destinatario@gmail.com'
msg.set_content('Aqui será a mensagem')