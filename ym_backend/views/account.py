from flask import Blueprint, render_template, redirect
from ym_backend import controller

account = Blueprint('account',__name__)

@account.route('/')
def index():
  return render_template('./index.html')

@account.route('/test')
def test():
  return controller.account.test()