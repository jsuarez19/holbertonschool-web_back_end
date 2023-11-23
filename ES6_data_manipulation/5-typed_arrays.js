export default function createInt8TypedArray(length, position, value) {
  if (position >= length) throw new Error('Position outside range');
  const buffer = new ArrayBuffer(length);
  const intArray = new Int8Array(buffer);
  intArray.setInt8(position, value);
  return buffer;
}
