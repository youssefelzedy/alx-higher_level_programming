#!/usr/bin/node

function factorial (n) {
  if (isNaN(n) || n === 0) {
    return 1;
  }
  return n * factorial(n - 1);
}

const nm1 = parseInt(process.argv[2]);
if (isNaN(nm1)) {
  console.log('1');
} else {
  console.log(factorial(nm1));
}
