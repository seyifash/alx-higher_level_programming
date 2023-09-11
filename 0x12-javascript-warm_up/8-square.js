#!/usr/bin/node
const args = process.argv[2];

const x = parseInt(args, 10);

if (!isNaN(x)) {
  for (let i = 0; i < x; i++) {
    let sqr = '';
    for (let j = 0; j < x; j++) {
      sqr += 'X';
    }
    console.log(sqr);
  }
} else {
  console.log('Missing size');
}
