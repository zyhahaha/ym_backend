#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from ym_backend import db

class Product(db.Model):
  __tablename__ = 'product'
  id = db.Column(db.Integer, primary_key=True)

  name = db.Column(db.String(200)) # 产品名称
  pic = db.Column(db.String(200)) # 产品图片
  summary = db.Column(db.Text()) # 产品简介
  remark = db.Column(db.Text()) # 备注
  url = db.Column(db.String(300)) # 备用

  def __repr__(self):
    return self.name
