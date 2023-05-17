const tree = require('tree-node-cli');

const string = tree('./', {
    allFiles: true,
    exclude: [/Static/, /__pycache__/, /node_modules/, /.git/, /.vscode/],
  });
  
console.log(string);