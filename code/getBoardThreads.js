const getBoardThreads = async (slug) => {
  const response = await fetch('https://dchan.org/${slug}/threads');
  const boarThreadsJSON = await response.json();
}