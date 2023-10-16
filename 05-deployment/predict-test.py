#!/usr/bin/env python
# coding: utf-8

import requests


url = 'http://localhost:9696/predict'

client = {"job": "retired", "duration": 445, "poutcome": "success"}
requests.post(url, json=client).json()


response = requests.post(url, json=client).json()
print(response)
