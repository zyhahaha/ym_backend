from ym_backend import db

class User(db.Model):
  __tablename__ = 'users'
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(80), unique=True)
  emai = db.Column(db.String(320), unique=True)
  password = db.Column(db.String(32), nullable=False)

  def __repr__(self):
    return self.username
