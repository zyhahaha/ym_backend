from ym_backend import app, controller
from flask import render_template
from .admin import admin
from .user import user
from .account import account
# from .common import common

app.register_blueprint(admin,url_prefix='/admin')
app.register_blueprint(user, url_prefix='/user')
app.register_blueprint(account, url_prefix='/account')

@app.route('/', methods=['GET'])
def index():
    return render_template('/upload.html')
@app.route('/upload', methods=['POST'])
def upload():
  return controller.common.upload_file()