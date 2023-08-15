#!/usr/bin/node

function callMeMoby(x, callMeMoby) {
  for (let i = 0; i < x; i++) {
    callMeMoby();
  }
}

module.exports.callMeMoby = callMeMoby;
