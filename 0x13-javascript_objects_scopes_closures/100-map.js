#!/usr/bin/node

const list = require('./100-data.js');
console.log(list.list);

const newList = list.list.map((x) => x * list.list.indexOf(x));

console.log(newList);
