from ym_backend import app, controller
from flask import render_template
from .account import account
from .product import product
# from .common import common

app.register_blueprint(account, url_prefix='/account')
app.register_blueprint(product, url_prefix='/product')

@app.route('/', methods=['GET'])
def index():
    return render_template('/upload.html')

@app.route('/upload', methods=['POST'])
def upload():
  return controller.common.upload_file()

@app.route('/sendEmail', methods=['POST'])
def sendEmail():
  return controller.common.send_email()