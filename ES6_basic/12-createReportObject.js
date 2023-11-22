export default function createReportObject(employeesList) {
  const output = {};
  output.allEmployees = {...employeesList};

  function getNumberOfDepartments(employeesList) {
    return Object.keys(employeesList).length;
  }

  return {
    output,
    getNumberOfDepartments
  };
}
