#!/usr/bin/node
const len = parseInt(process.argv[2]);
if (isNaN(len)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < len; i++) {
    let row = '';
    for (let j = 0; j < len; j++) {
      row += 'X';
    }
    console.log(row);
  }
}
