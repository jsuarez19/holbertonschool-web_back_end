export default function cleanSet(set, startString) {
  const wordsArray = [];
  if (!Array.isArray(set) || typeof startString !== 'string' || startString.length === 0) return '';

  for (const element of set) {
    if (element.startsWith(startString)) {
      const remainingPart = element.slice(startString.length);
      if (remainingPart.startsWith('-')) {
        wordsArray.push(element);
      } else {
        wordsArray.push(remainingPart);
    }
  }

  return wordsArray.join('-');
}
