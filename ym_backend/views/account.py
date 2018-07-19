import json
from flask import Blueprint, render_template, redirect, request
from ym_backend import controller, util

account = Blueprint('account',__name__)
accountCtrl = controller.Account(__name__)

@account.route('/')
def index():
  return render_template('./index.html')

# 注册
@account.route('/register', methods=['POST'])
def register():
  name = request.form['name']
  password = request.form['password']
  params = {
    'name': name,
    'password': password
  }
  return accountCtrl.register(params)

# 登录
@account.route('/login', methods=['POST'])
def login():
  name = request.form['name']
  password = request.form['password']
  params = {
    'name': name,
    'password': password
  }
  return accountCtrl.login(params)

# 查询用户信息
@account.route('/queryUser', methods=['POST', 'GET'])
def queryUser():
  token = request.headers.get('Token')
  isAuth = util.checkAuth(token)
  if not isAuth:
    return '未登录'
  if request.method == 'POST':
    name = request.form['name']
    params = {
      'name': name
    }
    return accountCtrl.queryUser(params)
  elif request.method == 'GET':
    return accountCtrl.queryUserAll()

# 修改用户信息
@account.route('/modifyUser', methods=['POST'])
def modifyUser():
  name = request.form['name']
  password = request.form['password']
  params = {
    'name': name,
    'password': password
  }
  return accountCtrl.modifyUser(params)

# 删除用户信息
@account.route('/delUser', methods=['POST'])
def delUser():
  id = request.form['id']
  return accountCtrl.delUser({'id': id})
