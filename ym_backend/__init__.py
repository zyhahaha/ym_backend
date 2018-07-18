from flask import Flask, url_for, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config.from_object('config')
# app.config.update(
#   MAIL_SERVER='smtp.163.com',
#   MAIL_USERNAME='18355403288@163.com',
#   MAIL_PASSWORD='zy854275944618'
# )
db = SQLAlchemy(app)
# from app import models,views
from ym_backend import views