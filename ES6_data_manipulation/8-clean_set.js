export default function cleanSet(set, startString) {
  const wordsArray = [];
  if (typeof set !== 'object' || typeof startString !== 'string' || startString.length === 0) return '';

  for (const element of set) {
    if (element.startsWith(startString)) {
      wordsArray.push(element.slice(startString.length));
    }
  }

  return wordsArray.join('-');
}
