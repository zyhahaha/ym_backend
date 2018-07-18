from .account_model import User
from .product_model import Product
from ym_backend import db

# 创建数据表
db.create_all()
