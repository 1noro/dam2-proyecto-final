const postReply = async (dataToSend, callback) => {
  const { slug, threadId } = dataToSend;
  const response = await fetch(`https://dchan.org/${slug}/thread/${threadId}`, {
    method: 'POST', 
    body: JSON.stringify(dataToSend)
  });
  const responseJSON = await response.json();
  callback(responseJSON);
}