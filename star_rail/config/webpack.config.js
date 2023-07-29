const path = require('path');


const starRailDir = path.resolve(__dirname, '..');
const rootDir = path.resolve(starRailDir, '..');


module.exports = {
  mode: 'production',
  entry: path.resolve(starRailDir, 'js', 'index.js'),
  output: {
    filename: 'star_rail.js',
    path: path.resolve(rootDir, 'static', 'dist', 'js'),
  },
};
