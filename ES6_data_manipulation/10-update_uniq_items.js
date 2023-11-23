export default function updateUniqueItems(map) {
  if (map instanceof Map){
    for (const [key, value] of map) {
      if (value === 1) {
        value = 100;
      };
    };
  } else {
    throw new Error('Cannot process');
  };
}
