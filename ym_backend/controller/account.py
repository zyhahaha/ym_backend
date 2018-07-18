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

class account(object):
  def __init__(self, arg):
    self.arg = arg

  def test():
    return 'account test'

  def register(params):
    return False

  def queryUser():
    users = User.query.filter(User.username == 'zhao1111').first()
    users = json.dumps(users, cls=AlchemyEncoder)
    print(users)
    return users

  def addUser():
    user = User(username = 'zhao1111', password = '123456')
    db.session.add(user)
    db.session.commit()
    users = User.query.all()
    users = json.dumps(users, cls=AlchemyEncoder)
    print(users)
    return users

  def modifyUser():
    user = User.query.filter(User.username == 'zhao').first()
    user.password = '654321'
    db.session.commit()

  def delUser():
    user = User.query.filter(User.username == 'zhao').first()
    db.session.delete(user)
    db.session.commit()
