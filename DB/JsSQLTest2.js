const mysql = require("mysql");
const fastcsv = require("fast-csv");
const fs = require("fs");
const ws = fs.createWriteStream("mysql_fastcsv.csv");

// Create a connection to the database
const connection = mysql.createConnection({
  host: "localhost",
  user: "root",
  password: "root",
  database: "project"
});

// open the MySQL connection
connection.connect(error => {
  if (error) throw error;

  // query data from MySQL
  connection.query("SELECT * FROM project", function(error, data, fields) {
    if (error) throw error;

    const jsonData = JSON.parse(JSON.stringify(data));
    console.log("jsonData", jsonData);

    // TODO: export to CSV file
    fastcsv
  .write(jsonData, { headers: true })
  .on("finish", function() {
    console.log("Write to mysql_fastcsv.csv successfully!");
  })
  .pipe(ws);
  });
});