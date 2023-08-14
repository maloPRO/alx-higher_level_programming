#!/usr/bin/node

for (let i = 0; i < process.argv[2]; i++) {
  if ((!process.argv[2]) || (process.argv[2] < 0)) {
    console.log('Missing number of occurrences');
  } else {
    console.log('C is fun');
  }
}
