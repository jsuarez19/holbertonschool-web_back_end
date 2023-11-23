export default function getListStudentsIds(list) {
  if (!Array.isArray(list)) return [];
  const ids = list.map((list) => list.id);
  return ids;
}
