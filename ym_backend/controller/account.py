from sqlalchemy.ext.declarative import DeclarativeMeta
import json
from ym_backend import model, db
User = model.User

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

class Account(object):
  def __init__(self, arg):
    self.arg = arg

  def register(self, params):
    if params and params['name'] and params['password']:
      username = params['name']
      password = params['password']
      user = User(username = username, password = password)
      db.session.add(user)
      db.session.commit()
      users = User.query.filter(User.username == username).first()
      users = self.jsonHandle(users)
      return users
    else:
      return self.jsonHandle({ 'err': 400, 'msg': '参数不能为空' })

  def queryUser(self, params):
    name = ''
    if params and params['name']:
      name = params['name']
    users = User.query.filter(User.username == name).first()
    users = self.jsonHandle(users)
    print(users)
    return users

  # 查询所有
  def queryUserAll(self):
    users = User.query.all()
    users = self.jsonHandle(users)
    return users

  def modifyUser(self, params):
    if params and params['name'] and params['password']:
      username = params['name']
      password = params['password']
      user = User.query.filter(User.username == username).first()
      user.password = password
      db.session.commit()
      users = User.query.filter(User.username == username).first()
      users = self.jsonHandle(users)
      return users
    else:
      return self.jsonHandle({ 'err': 400, 'msg': '参数不能为空' })

  def delUser(self, params):
    if params and params['id']:
      id = params['id']
      user = User.query.filter(User.id == id).first()
      db.session.delete(user)
      db.session.commit()
      result = { 'code': 200, 'msg': '删除成功' }
      result = self.jsonHandle(result)
      return result
    else:
      return self.jsonHandle({ 'err': 400, 'msg': '参数不能为空' })

  def jsonHandle(self, obj):
    return json.dumps(obj, cls=AlchemyEncoder, ensure_ascii=False)
