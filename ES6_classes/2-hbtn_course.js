export default class HolbertonCourse {
  constructor(name, length, students){
    if (typeof name !== 'string') throw TypeError('Name size must be a string');
    if (typeof length !== 'number') throw TypeError('Length size must be a number');
    if (typeof students !== 'array') throw TypeError('Students size must be a array');
    
    this._name = name;
    this._length = length;
    this._students = students;
  }

  get name() {
    return this._name;
  }
  get length() {
    return this._length;
  }
  get students() {
    return this._students;
  }

  set name(newName) {
    if (typeof newName !== 'string') throw TypeError('Name size must be a string');
    this._name = newName
  }
  set length(newLength) {
    if (typeof newLength  !== 'number') throw TypeError('Length size must be a number');
    this._name = newLength
  }
  set students(newStudents) {
    if (typeof newStudents !== 'array') throw TypeError('Students size must be a array');
    this._name = newStudents
  }

}
