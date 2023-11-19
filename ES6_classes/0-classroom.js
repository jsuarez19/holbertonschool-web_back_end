export default class ClassRoom {
  constructor(maxStudentsSize) {
    if (typeof maxStudentsSize !== 'Number') throw TypeError('Max Student size must be a number');
    this._maxStudentsSize = maxStudentsSize;
  }
}
