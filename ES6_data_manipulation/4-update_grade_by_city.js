export default function updateStudentGradeByCity(list, city, newGrades) {
  const studentsByLocation = list
    .filter((student) => student.location === city)
    .map((student) => {
      // Use filter to find all grades for the student in newGrades
      const studentGrades = newGrades.filter((grade) => grade.studentId === student.id);
      // condición ? valor_si_verdadero : valor_si_falso
      const grade = studentGrades.length > 0 ? studentGrades[0].grade : 'N/A';
      return { ...student, grade };
    });
  return studentsByLocation;
}
