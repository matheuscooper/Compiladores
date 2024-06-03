
const fs = require('fs');

const argumentos = process.argv;
//console.log(argumentos);

fs.readdir(argumentos[2], (err, files) => {
  if (err)
    console.log(err);
  else {
    files.forEach(file => {
      console.log(file);
    })
  }
})