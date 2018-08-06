#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from ym_backend import db

class Account(db.Model):
  __tablename__ = 'db_account'
  uuid = db.Column(db.Integer, primary_key=True)

  token = db.Column(db.String(50), unique=True)
  username = db.Column(db.String(80))
  emai = db.Column(db.String(320))
  password = db.Column(db.String(32), nullable=False)

  def __repr__(self):
    return self.username
