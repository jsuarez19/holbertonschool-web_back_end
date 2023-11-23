export default function hasValuesFromArray(set, array) {
  for (const element in array) {
    if (!set.has(element)) return false;
  }
  return true;
}
