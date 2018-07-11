from flask import Blueprint, render_template, redirect
from ym_backend import controller

user = Blueprint('user',__name__)

@user.route('/index')
def index():
  return render_template('./index.html')

@user.route('/add')
def add():
  return 'user_add'

@user.route('/show')
def show():
  return 'user_show'

@user.route('/test')
def test():
  return controller.user.test2()