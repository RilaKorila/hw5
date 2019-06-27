#!/usr/bin/env python
# -*- coding: utf-8 -*-

from google.appengine.api import urlfetch
import json
from flask import Flask, render_template, request

app = Flask(__name__)
app.debug = True

networkJson = urlfetch.fetch("http://tokyo.fantasy-transit.appspot.com/net?format=json").content  # ウェブサイトから電車の線路情報をJSON形式でダウンロードする
network = json.loads(networkJson.decode('utf-8'))  # JSONとしてパースする（stringからdictのlistに変換する）

@app.route('/')
# / のリクエスト（例えば http://localhost:8080/ ）をこの関数で処理する。
# ここでメニューを表示をしているだけです。
def root():
  return render_template('hello.html')

@app.route('/pata')
# /pata のリクエスト（例えば http://localhost:8080/pata ）をこの関数で処理する。
# これをパタトクカシーーを処理するようにしています。
def pata():
  # とりあえずAとBをつなぐだけで返事を作っていますけど、パタタコカシーーになるように自分で直してください！
  first_sentence = request.args.get('a', '')
  second_sentence = request.args.get('b', '')

  pata = pata_main(first_sentence, second_sentence)

  # pata.htmlのテンプレートの内容を埋め込んで、返事を返す。
  return render_template('pata.html', pata=pata)

@app.route('/norikae')
# /norikae のリクエスト（例えば http://localhost:8080/norikae ）をこの関数で処理する。
# ここで乗り換え案内をするように編集してください。
def norikae():
  return render_template('norikae.html', network=network)



#------------------------patatokutashi--------------------------------------
def sentence_to_list(sentence):
  list = []
  for char in sentence:
    list.append(char)
  return list


def adjust_length(first, second):
  if len(first) == len(second):
    return
  elif len(first) < len(second):
    first.append('0')
    adjust_length(first, second)
  else:
    second.append('0')
    adjust_length(first, second)


def pata_main(first, second):
  first_list = sentence_to_list(first)
  second_list = sentence_to_list(second)

  # print(first_list)
  # print(second_list)
  # print(first_list[0])

  adjust_length(first_list, second_list)
  result_list = []

  i = 0
  length = len(first_list)
  for i in range(0, length):
    if first_list[i] != '0':
      result_list.append(first_list[i])
    if second_list[i] != '0':
      result_list.append(second_list[i])

  result_string = ''
  for char in result_list:
    result_string += char

  return result_string

#------------------------------- norikae -------------------------------------
