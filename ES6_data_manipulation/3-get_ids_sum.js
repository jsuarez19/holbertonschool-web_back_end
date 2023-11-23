export default function getStudentIdsSum(list) {
  const ids = list.map((list) => list.id);

  const sum = ids.reduce((accumulator, currentValue) => {
    return accumulator + currentValue;
  })
  
  return sum;
}