from flask import request
from flask_mail import Mail, Message
from ym_backend import app

mail = Mail(app)

def send_email():
  if request.method == 'POST':
    msg = Message('Hello',
                  sender=('Zhaoyang', '18355403288@163.com'),
                  recipients=['980355088@qq.com'])
    msg.html = '<h1>Hello World</h1>'
    mail.send(msg)
    return 'Successful'
  else:
    return "error"