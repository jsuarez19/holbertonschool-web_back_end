export default function hasValuesFromArray(set, array) {
  for (element in array) {
    if (!set.has(element)) return false;
  }
  return true;
}
