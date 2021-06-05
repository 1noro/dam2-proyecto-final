@app.route('/<slug>/thread/<thread_id>', methods=['POST'])
def post_reply(slug, thread_id):
  formData = request.get_json()
  mydb = get_mydb()
  mycursor = mydb.cursor()
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