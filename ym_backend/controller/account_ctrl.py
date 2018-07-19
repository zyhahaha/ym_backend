#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import make_response
import json
import time
import hashlib
from ym_backend import model, db, util
AccountModel = model.Account
AlchemyEncoder = util.AlchemyEncoder

class Account(object):
  def __init__(self, arg):
    self.arg = arg

  # 注册
  def register(self, params):
    if params and params['name'] and params['password']:
      username = params['name']
      password = params['password']
      user = AccountModel(username = username, password = password)
      db.session.add(user)
      db.session.commit()
      # users = User.query.filter(User.username == username).first()
      userResult = self.responseHandle(user)
      return userResult
    else:
      return self.responseHandle({ 'err': 400, 'msg': '参数不能为空' })

  #登录
  def login(self, params):
    hashStr = str(time.time()) + 'ym'
    token = hashlib.md5(hashStr.encode('utf-8')).hexdigest()
    if params and params['name'] and params['password']:
      username = params['name']
      password = params['password']
      users = AccountModel.query.filter_by(username = username, password = password).first()
      if not users:
        return self.responseHandle({ 'code': 400, 'msg': '登录失败' })
      else:
        # users = self.responseHandle(users)
        # users = json.decoder(users)
        # id = users.id
        users.token = token
        db.session.commit()
        headers = {
          'Set-Cookie': 'token=' + token
        }
        return self.responseHandle({ 'code': 200, 'token': token, 'msg': '登录成功' }, headers = headers)
    else:
      return self.responseHandle({ 'err': 400, 'msg': '参数不能为空' })

  # 查询用户信息
  def queryUser(self, params):
    name = ''
    if params and params['name']:
      name = params['name']
    users = AccountModel.query.filter(AccountModel.username == name).first()
    users = self.responseHandle(users)
    return users

  # 查询所有
  def queryUserAll(self):
    users = AccountModel.query.all()
    users = self.responseHandle(users)
    return users

  # 修改用户信息
  def modifyUser(self, params):
    if params and params['name'] and params['password']:
      username = params['name']
      password = params['password']
      user = AccountModel.query.filter(AccountModel.username == username).first()
      user.password = password
      db.session.commit()
      users = AccountModel.query.filter(AccountModel.username == username).first()
      users = self.responseHandle(users)
      return users
    else:
      return self.responseHandle({ 'err': 400, 'msg': '参数不能为空' })

  # 删除用户信息
  def delUser(self, params):
    if params and params['id']:
      id = params['id']
      user = AccountModel.query.filter(AccountModel.id == id).first()
      db.session.delete(user)
      db.session.commit()
      result = { 'code': 200, 'msg': '删除成功' }
      result = self.responseHandle(result)
      return result
    else:
      return self.responseHandle({ 'err': 400, 'msg': '参数不能为空' })

  # 处理响应
  def responseHandle(self, obj, **conf):
    jsonStr = json.dumps(obj, cls = AlchemyEncoder, ensure_ascii = False)
    response = make_response(jsonStr)
    response.headers['Content-Type'] = 'application/json'
    if conf and conf['headers']:
      headers = conf['headers']
      for key, value in headers.items():
        response.headers[key] = value
    return response
