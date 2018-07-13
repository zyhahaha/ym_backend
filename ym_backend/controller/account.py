from sqlalchemy.ext.declarative import DeclarativeMeta
import json
from ym_backend import model, db
User = model.User
class account(object):
  def __init__(self, arg):
    self.arg = arg

  def test():
    return 'account test'

  def register(params):
    return False

  def queryUser():
    User.query.filter(User.username == 'zhao').first()

  def addUser():
    user = User(username = 'zhao11', password = '123456')
    db.session.add(user)
    db.session.commit()
    users = User.query.all()
    return users

  def modifyUser():
    user = User.query.filter(User.username == 'zhao').first()
    user.password = '654321'
    db.session.commit()

  def delUser():
    user = User.query.filter(User.username == 'zhao').first()
    db.session.delete(user)
    db.session.commit()

class AlchemyEncoder(json.JSONEncoder):
  def default(self, obj):
    if isinstance(obj.__class__, DeclarativeMeta):
        # an SQLAlchemy class
        fields = {}
        for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
            data = obj.__getattribute__(field)
            try:
                json.dumps(data)     # this will fail on non-encodable values, like other classes
                fields[field] = data
            except TypeError:    # 添加了对datetime的处理
                if isinstance(data, datetime.datetime):
                    fields[field] = data.isoformat()
                elif isinstance(data, datetime.date):
                    fields[field] = data.isoformat()
                elif isinstance(data, datetime.timedelta):
                    fields[field] = (datetime.datetime.min + data).time().isoformat()
                else:
                    fields[field] = None
        # a json-encodable dict
        return fields

    return json.JSONEncoder.default(self, obj)
