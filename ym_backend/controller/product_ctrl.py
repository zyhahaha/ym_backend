from sqlalchemy.ext.declarative import DeclarativeMeta
from flask import make_response
import json
from ym_backend import model, db
ProductModel = model.Product

# sql json处理
class AlchemyEncoder(json.JSONEncoder):
  def default(self, obj):
    if isinstance(obj.__class__, DeclarativeMeta):
        # an SQLAlchemy class
        fields = {}
        for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
            data = obj.__getattribute__(field)
            try:
                json.dumps(data) # this will fail on non-encodable values, like other classes
                fields[field] = data
            except TypeError:
                fields[field] = None
        # a json-encodable dict
        return fields

    return json.JSONEncoder.default(self, obj)

class Product(object):
  def __init__(self, arg):
    self.arg = arg

  # 添加商品
  def addProduct(self, params):
    if params and params['name']:
      name = params['name']
      pic = params['pic']
      # summary = params['summary']
      # remark = params['remark']
      # url = params['url']
      product = ProductModel(name = name, pic = pic)
      db.session.add(product)
      db.session.commit()
      # # product = ProductModel.query.filter(ProductModel.username == username).first()
      productResult = self.responseHandle(product)
      return productResult
    else:
      return self.responseHandle({ 'err': 400, 'msg': '参数不能为空' })

  # 查询用户信息
  def queryProduct(self, params):
    name = ''
    if params and params['name']:
      name = params['name']
    product = ProductModel.query.filter(ProductModel.name == name).first()
    product = self.responseHandle(product)
    return product

  # 查询所有
  def queryProductAll(self):
    products = ProductModel.query.all()
    products = self.responseHandle(products)
    return products

  # 修改用户信息
  def modifyProduct(self, params):
    if params and params['name'] and params['pic']:
      name = params['name']
      pic = params['pic']
      product = ProductModel.query.filter(ProductModel.name == name).first()
      product.pic = pic
      db.session.commit()
      # users = ProductModel.query.filter(ProductModel.name == name).first()
      productResult = self.responseHandle(product)
      return productResult
    else:
      return self.responseHandle({ 'err': 400, 'msg': '参数不能为空' })

  # 删除用户信息
  def delProduct(self, params):
    if params and params['id']:
      id = params['id']
      product = ProductModel.query.filter(ProductModel.id == id).first()
      db.session.delete(product)
      db.session.commit()
      result = { 'code': 200, 'msg': '删除成功' }
      result = self.responseHandle(result)
      return result
    else:
      return self.responseHandle({ 'err': 400, 'msg': '参数不能为空' })

  # 处理响应
  def responseHandle(self, obj):
    jsonStr = json.dumps(obj, cls=AlchemyEncoder, ensure_ascii=False)
    response = make_response(jsonStr)
    response.headers['Content-Type'] = 'application/json' 
    return response
