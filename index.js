var json_data = require("./Complet.json")
var result = [];
var names = ["Breydi", "Jose", "raul", "alberto"]

for(var i in json_data)
    //console.log(json_data [i])
    result.push(json_data [i])


//////////////////////////////////////////////////////////////////////////////
//result.push([i, json_data [i]]);
console.log(result[0][1][0])
console.log(result[0][1][0].nodes.length)

//console.log(result[0][1].length)

let nn = ""
resulta[0][0].forEach((element, i) => {
    nn += `${i},${element.lat},${element.lon}\n`
    //console.log(nodes)
})

//console.log(namee)
fs = require('fs');
fs.writeFile('nodes.txt', nn, function (err) {
  if (err) return console.log(err);
  //console.log(`${namee} > helloworld.txt`);
});