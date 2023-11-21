export default function createEmployeesObject(departmentName, employees) {
  const output = { [departmentName]: [...employees] };
  return output;
}
