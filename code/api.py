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

class Thread:
    def __init__(self, id, subject, author, comment, fileurl, published, sticky, closed):
        self.id = id;
        self.subject = subject;
        self.author = author;
        self.comment = comment;
        self.fileurl = fileurl;
        self.published = published;
        self.sticky = sticky;
        self.closed = closed;
    def to_JSON(self):
        return json.dumps(self, default=lambda o: o.__dict__)

class Board:
    def __init__(self, slug, name, thread_list):
        self.slug = slug;
        self.name = name;
        self.thread_list = thread_list;
    def to_JSON(self):
        return json.dumps(self, default=lambda o: o.__dict__)

@app.route('/board', methods=["GET"])
def get_boards():
    board_list = []
    # board_list.append(Board('a', 'Anime & Manga', None))
    # board_list.append(Board('b', 'Random', None))
    # board_list.append(Board('g', 'Technology', None))
    mydb = get_mydb()
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM BOARD")
    myresult = mycursor.fetchall()
    for col in myresult:
        board_list.append(Board(col[0], col[1], None))
    encoded_JSON = json.dumps(jsonpickle.encode(board_list, unpicklable=False))
    decoded_JSON = json.loads(encoded_JSON)
    return app.response_class(
        response = decoded_JSON,
        status = 200,
        mimetype = 'application/json'
    )
    

@app.route('/<slug>', methods=["GET"])
def get_threads(slug):
    thread_list = []
    thread_list.append(Thread(
        81930017,
        '/pcbg/ - PC Building General',
        'Anonymous',
        '''>UPGRADE & BUILD ADVICE
Post build "list" or current specs including MONITOR
Convient lister: https://pcpartpicker.com/
Provide specific use cases (e.g. gaming, editing, rendering)
State budget and region''',
        'https://i.dcdn.org/g/1622853294379s.jpg',
        '06/05/21(Sat)02:34:54',
        False,
        False
    ))
    board = Board('g', 'Technology', thread_list)
    encoded_JSON = json.dumps(board.to_JSON())
    decoded_JSON = json.loads(encoded_JSON)
    return app.response_class(
        response = decoded_JSON,
        status = 200,
        mimetype = 'application/json'
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0')
    print('program finnished')