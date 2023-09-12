#!/usr/bin/node

const list = require('./100-data');
console.log(list.list);

const newList = list.list.map((item, idx) => item * idx);
console.log(newList);
