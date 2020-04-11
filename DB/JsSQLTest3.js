
var mysql = require('mysql');
var DataFrame = require('dataframe-js').DataFrame;

var con = mysql.createConnection({
  host: "localhost",
  user: "root",
  password: "root",
  database: "project"
});

con.connect(function(err) {
  if (err) throw err;
  con.query("SELECT * FROM project", function (err, result, fields) {
    if (err) throw err;   
    const df = new DataFrame(result);
    var num = df.count();
    console.log(num);
    df.show(); 		
  });
});
