const getThreads = async (slug, callback) => {
  const response = await fetch(`https://dchan.org/${slug}`);
  const threadsJSON = await response.json();
  callback(threadsJSON);
}