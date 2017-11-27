# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 14:56:08 2017

@author: User
"""

import os
import tempfile
import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--key", help="display a square of a given number")
parser.add_argument("--val", help="increase output verbosity")

args = parser.parse_args()
if args.key:
    storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
    data = []
    if (os.path.isfile(storage_path)):
        with open(storage_path, 'r') as f:
            data = json.load(f)
    else:
        data = json.loads('[]')
    if args.val:        
        new_elem_dict = {'key': args.key, 'value': args.val}
        data.append(new_elem_dict)
        with open(storage_path, 'w') as f:
            print (data)
            json.dump(data, f)
    else:        
        if (len(data) > 0):
            result = [str(elem['value']) for elem in data if elem['key'] == args.key]
            print (', '.join(res for res in result))