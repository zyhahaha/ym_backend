#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from sqlalchemy.ext.declarative import DeclarativeMeta
import json
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

def sqlJsonDump(obj):
    return json.dumps(obj, cls = AlchemyEncoder, ensure_ascii = False)