#!/usr/bin/node
const len = parseInt(process.argv[2]);
if (!len) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < len; i++) {
    let row = '';
    for (let j = 0; j < len; j++) {
      row += 'X';
    }
    console.log(row);
  }
}
