#!/usr/bin/node
const args = process.argv[2];
if (args === undefined) {
  console.log('Not a number');
} else {
  const convertArg = parseInt(args, 10);

  if (!isNaN(convertArg)) {
    console.log(`My number: ${convertArg}`);
  } else {
    console.log('Not a number');
  }
}
