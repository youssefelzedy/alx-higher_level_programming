#!/usr/bin/node
const num = parseInt(process.argv[2]);
if (!num) {
  console.log('No argument');
} else {
  console.log(`${num}`);
}
