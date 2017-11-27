# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 17:53:26 2017

@author: User
"""
import json

def to_json(func):
    def wrapper(*args, **kwargs):
        return json.dumps(func(*args, **kwargs))
    return wrapper

@to_json
def get_data(param):
  return {
    'data': param
  }
  
result = get_data(42)
print (result)  # вернёт '{"data": 42}'

print (get_data([1,2,3]))