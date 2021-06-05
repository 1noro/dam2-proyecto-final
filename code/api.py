#!/usr/bin/python

import os
import json
import time
import jsonpickle
import mysql.connector

from multiprocessing import Process
from datetime import datetime
from flask import Flask, request  # python-flask

app = Flask(__name__)

def get_mydb():
  return mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456789",
    database="DCHAN"
  )

class ThreadDTO:
  def __init__(self, id, subject, author, comment, fileurl, published, sticky, closed):
    self.id = id;
    self.subject = subject;
    self.author = author;
    self.comment = comment;
    self.fileurl = fileurl;
    self.published = published.strftime('%c');
    self.sticky = sticky;
    self.closed = closed;
  def to_JSON(self):
    return json.dumps(self, default=lambda o: o.__dict__)

class BoardDTO:
  def __init__(self, slug, name, thread_list):
    self.slug = slug;
    self.name = name;
    self.thread_list = thread_list;
  def to_JSON(self):
    return json.dumps(self, default=lambda o: o.__dict__)

@app.route('/board', methods=['GET'])
def get_boards():
  board_list = []
  mydb = get_mydb()
  mycursor = mydb.cursor()
  mycursor.execute("SELECT * FROM BOARD")
  myresult = mycursor.fetchall()
  for col in myresult:
    board_list.append(BoardDTO(col[0], col[1], None))
  encoded_JSON = json.dumps(jsonpickle.encode(board_list, unpicklable=False))
  decoded_JSON = json.loads(encoded_JSON)
  mycursor.close()
  mydb.close()
  return app.response_class(
    response = decoded_JSON,
    status = 200,
    mimetype = 'application/json'
  )

@app.route('/<slug>', methods=['GET'])
def get_threads(slug):
  thread_list = []
  mydb = get_mydb()
  mycursor = mydb.cursor()
  mycursor.execute("SELECT name FROM BOARD WHERE slug = '{}'".format(slug))
  board_name = mycursor.fetchone()[0]
  mycursor.execute("SELECT * FROM THREAD WHERE board = '{}'".format(slug))
  myresult = mycursor.fetchall()
  for col in myresult:
    thread_list.append(ThreadDTO(*col[:-2]))
  board = BoardDTO(slug, board_name, thread_list)
  encoded_JSON = json.dumps(board.to_JSON())
  decoded_JSON = json.loads(encoded_JSON)
  mycursor.close()
  mydb.close()
  return app.response_class(
    response = decoded_JSON,
    status = 200,
    mimetype = 'application/json'
  )

@app.route('/<slug>/thread/<thread_id>', methods=['POST'])
def post_reply(slug, thread_id):
  formData = request.get_json()
  mydb = get_mydb()
  mycursor = mydb.cursor()
  # sql = "CALL insert_post('{}', '{}', '{}', {});".format(
  #   formData['author'],
  #   formData['comment'],
  #   formData['imageurl'],
  #   thread_id
  # )
  args = (
    formData['author'],
    formData['comment'],
    formData['imageurl'],
    thread_id
  )
  mycursor.callproc('insert_post', args)
  mycursor.close()
  mydb.close()
  return app.response_class(
    response = '{"info": "posted"}',
    status = 201,
    mimetype = 'application/json'
  )

if __name__ == '__main__':
  app.run(host='0.0.0.0')
  print('program finnished')