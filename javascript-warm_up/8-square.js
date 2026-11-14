#!/usr/bin/node

const size = parseInt(process.argv[2]);

if (isNaN(size)) {
  console.log('Missing size');
} else {
  let i = 0;

  while (i < size) {
    let row = '';
    let j = 0;

    while (j < size) {
      row += 'X';
      j++;
    }

    console.log(row);
    i++;
  }
}
