#!/bin/python
# -*- coding: utf-8 -*-
# filename: basic.py

import os

script_dir = os.path.split(os.path.realpath(__file__))[0]                   


def get():

  file = open(script_dir + '/token', 'r')
  token = file.read()
  return token
