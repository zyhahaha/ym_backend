import json
from flask import Blueprint, render_template, redirect, request
from ym_backend import controller

product = Blueprint('product',__name__)
ProductCtrl = controller.Product(__name__)

@product.route('/')
def index():
  return render_template('./index.html')

# 注册
@product.route('/addProduct', methods=['POST'])
def addProduct():
  name = request.form['name']
  pic = request.form['pic']
  params = {
    'name': name,
    'pic': pic
  }
  return ProductCtrl.addProduct(params)

# 查询用户信息
@product.route('/queryProduct', methods=['POST', 'GET'])
def queryProduct():
  if request.method == 'POST':
    name = request.form['name']
    params = {
      'name': name
    }
    return ProductCtrl.queryProduct(params)
  elif request.method == 'GET':
    return ProductCtrl.queryProductAll()

# 修改用户信息
@product.route('/modifyProduct', methods=['POST'])
def modifyProduct():
  name = request.form['name']
  pic = request.form['pic']
  params = {
    'name': name,
    'pic': pic
  }
  return ProductCtrl.modifyProduct(params)

# 删除用户信息
@product.route('/delProduct', methods=['POST'])
def delProduct():
  id = request.form['id']
  return ProductCtrl.delProduct({'id': id})
