export default function getStudentsByLocation(list, city) {
  const result = list.filter((student) => student.location === city);
  return result;
}
