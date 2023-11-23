export default function cleanSet(set, startString) {
  const wordsArray = [];
  if (typeof set !== 'object' || typeof startString !== 'string' || startString.length === 0) return '';

  for (const element of set) {
    if (element.startsWith(startString)) {
      const remainingPart = element.slice(startString.length);
      if (remainingPart.startsWith('-')) {
        wordsArray.push(element);
      } else {
        wordsArray.push(remainingPart);
      }
    }
  }
  return wordsArray.join('-');
}
