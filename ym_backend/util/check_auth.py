#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from ym_backend import model, db
AccountModel = model.Account

def checkAuth(token):
  if not token:
    return False
  users = AccountModel.query.filter_by(token = token).first()
  if not users:
    return False
  else:
    return True