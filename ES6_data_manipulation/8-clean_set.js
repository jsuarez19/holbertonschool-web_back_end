export default function cleanSet(set, startString) {
  const valuesArray = Array.from(set);
  const filteredArray = valuesArray
    .filter((value) => value.startsWith(startString));
  const slicedWords = filteredArray
    .map((word) => word.slice(startString.length));
  const result = slicedWords.join('-');
  return result;
}
