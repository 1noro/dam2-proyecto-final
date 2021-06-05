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