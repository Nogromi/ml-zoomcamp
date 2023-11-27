#!/usr/bin/env python
# coding: utf-8

import tflite_runtime.interpreter as tflite
from io import BytesIO
from urllib import request
from PIL import Image
import numpy as np

interpreter = tflite.Interpreter(model_path='wasps-bees.tflite')
interpreter.allocate_tensors()
input_index = interpreter.get_input_details()[0]['index']
output_index = interpreter.get_output_details()[0]['index']

def download_image(url):
    with request.urlopen(url) as resp:
        buffer = resp.read()
    stream = BytesIO(buffer)
    img = Image.open(stream)
    return img

def prepare_image(img, target_size):
    if img.mode != 'RGB':
        img = img.convert('RGB')
    img = img.resize(target_size, Image.NEAREST)
    return img

def preprocess_input(x):
    x /= 255
    # x -= 1.
    return x

def read_img(url):
    img=download_image(url)
    img=prepare_image(img,(150,150))
    x = np.array(img, dtype='float32')
    X = np.array([x])
    X = preprocess_input(X)
    return X

def predict(url):
    X = read_img(url)
    interpreter.set_tensor(input_index, X)
    interpreter.invoke()
    preds = interpreter.get_tensor(output_index)
    result_probability = preds[0].tolist()

    return result_probability


def lambda_handler(event, context):
    url = event['url']
    result = predict(url)
    return result
