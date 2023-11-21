export default function appendToEachArrayValue(array, appendString) {
  const arrayCopy = [];
  for (let value of array) {
    arrayCopy.push(appendString + value);
  }

  return arrayCopy;
}
