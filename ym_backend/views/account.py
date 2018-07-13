import json
from flask import Blueprint, render_template, redirect
from ym_backend import controller

account = Blueprint('account',__name__)

@account.route('/')
def index():
  return render_template('./index.html')

@account.route('/test')
def test():
  return controller.account.test()

@account.route('/queryUser')
def queryUser():
  return controller.account.queryUser()

@account.route('/addUser')
def addUser():
  users = controller.account.addUser()
  usersJson = json.dumps(users)
  return usersJson

@account.route('/modifyUser')
def modifyUser():
  return controller.account.modifyUser()

@account.route('/delUser')
def delUser():
  return controller.account.delUser()
