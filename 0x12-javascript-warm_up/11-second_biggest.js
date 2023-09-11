#!/usr/bin/node

let arr = [];

if (process.argv.length === 2 || process.argv.length === 3) {
  console.log(0);
} else if (process.argv.length > 3){
  for (let i = 2; i < process.argv.length; i++) {
    arr.push(process.argv[i]);
  }
}
newArr = arr.sort((a, b) => b - a);
console.log(newArr[1]);
