const path = require('path');

const homeDir = path.resolve(__dirname, '..');


module.exports = {
  mode: 'production',
  entry: path.resolve(homeDir, 'client', 'index.js'),
  output: {
    filename: 'star_rail.js',
    path: path.resolve(homeDir, 'static', 'dist'),
    clean: true,
  },
};
