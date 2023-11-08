#!/usr/bin/python3
"""Load, add, save"""
import sys


save = __import__('5-save_to_json_file').save_to_json_file
load = __import__('6-load_from_json_file').load_from_json_file

args = list(sys.argv[1:])

try:
    my_list = load("add_item.json")
except Exception:
    my_list = []

my_list.extend(args)
save(my_list, "add_item.json")
