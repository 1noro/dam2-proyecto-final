/*
 * upperOrNot: Given a character and its predecessor,
 * it returns that same character converted to upper
 * or lower case based on the ASCII value of its
 * predecessor.
 */
const upperOrNot = (previous, actual) => {
  if (previous.charCodeAt(0) % 2 !== 0) {
      return actual.toUpperCase();
  }
  return actual;
}

/*
 * strToNumber: Given a character string returns a 
 * string of numbers, based on the value of the 
 * characters in the ASCII table.
 */
const strToNumber = (str) => {
  return [...str].map(
    (char) => char.charCodeAt(0) % 10
  ).join('');
}

export { upperOrNot, strToNumber };