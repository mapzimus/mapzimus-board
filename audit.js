const fs = require('fs');
const raw = fs.readFileSync('data.js','utf8');
const D = eval('(' + raw.replace('const D =','').replace(/;\s*\/\/ end D\s*$/,'') + ')');

// Use a Map instead of object to avoid prototype issues
var seen = new Map();
var dupes = [];
D.forEach(function(d, i) {
  if (seen.has(d.id)) {
    dupes.push({id: d.id, first: seen.get(d.id), second: i});
  } else {
    seen.set(d.id, i);
  }
});

console.log('Total D:', D.length);
console.log('Map size (unique):', seen.size);
console.log('Duplicates:', dupes.length);
dupes.forEach(function(d) {
  console.log('  DUPE: "' + d.id + '" at ' + d.first + ' and ' + d.second);
  console.log('  A title:', D[d.first].title);
  console.log('  B title:', D[d.second].title);
});

// Also check if there are any IDs with invisible/unusual chars
D.forEach(function(d, i) {
  if (d.id.length !== d.id.trim().length) {
    console.log('WHITESPACE in id at ' + i + ': [' + d.id + ']');
  }
  for (var c = 0; c < d.id.length; c++) {
    var code = d.id.charCodeAt(c);
    if (code > 127) {
      console.log('NON-ASCII in id at ' + i + ': char ' + c + ' code ' + code + ' id=' + d.id);
    }
  }
});
