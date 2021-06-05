@app.route('/<slug>', methods=['GET'])
def get_threads(slug):
  thread_list = []
  mydb = get_mydb()
  mycursor = mydb.cursor()
  mycursor.execute(
    "SELECT name FROM BOARD WHERE slug = '{}'".format(slug)
  )
  board_name = mycursor.fetchone()[0]
  mycursor.execute(
    "SELECT * FROM THREAD WHERE board = '{}'".format(slug)
  )
  myresult = mycursor.fetchall()
  for col in myresult:
    thread_list.append(Thread(*col[:-2]))
  board = Board(slug, board_name, thread_list)
  encoded_JSON = json.dumps(board.to_JSON())
  decoded_JSON = json.loads(encoded_JSON)
  mycursor.close()
  mydb.close()
  return app.response_class(
    response = decoded_JSON,
    status = 200,
    mimetype = 'application/json'
  )