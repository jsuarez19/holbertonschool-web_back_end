export default function getStudentIdsSum(list) {
  const ids = list.map((list) => list.id);

  const sum = ids.reduce((accumulator, currentValue) => accumulator + currentValue, 0);

  return sum;
}
