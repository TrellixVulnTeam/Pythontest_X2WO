#!/usr/bin/python
# -*- coding: utf-8 -*-

import basic_grammar
import os
if __name__ == "__main__":
	age = 30
	name = "bill"
	print("%s is %d years old" % (name, age))
	print(basic_grammar.x)

print(os.path.realpath(__file__))
print(os.path.split(os.path.realpath(__file__)))