export default function createEmployeesObject(departmentName, employees) {
  output = {[departmentName]: [...employees]};
  return output;
}
