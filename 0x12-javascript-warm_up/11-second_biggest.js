#!/usr/bin/node
const args = process.argv.slice(2).map(arg => parseInt(arg, 10));

if (args.length <= 1) {
  console.log(0);
} else {
  const uniqueArgs = [...new Set(args)];
  const sortedArgs = uniqueArgs.sort((a, b) => b - a);
  console.log(sortedArgs[1]);
}
