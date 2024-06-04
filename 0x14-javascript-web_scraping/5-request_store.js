#!/usr/bin/node

const url = process.argv[2];

fetch(url).then((response) => {
  return response.body;
}).then((data) => {
    console.log(data)
});
