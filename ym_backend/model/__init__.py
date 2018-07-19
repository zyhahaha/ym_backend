from .account_model import Account
from .product_model import Product
from ym_backend import db

# 创建数据表
db.create_all()
