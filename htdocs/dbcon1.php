<!DOCTYPE html>
<html>
<head>
	<script src="chartsloader.js"></script>
<script type="text/javascript">

var dbr = <?php
$servername = "localhost";
$username = "root";
$password = "root";
$dbname = "project";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}


$sql = "SELECT * FROM project";
$result = $conn->query($sql);


$conn->close();
echo json_encode($result->fetch_all());

?>;

console.log(typeof dbr);

google.charts.load('current', {packages: ['corechart']});
    google.charts.setOnLoadCallback(drawChart);

    function drawChart() {
      // Define the chart to be drawn.
      
      
      //const jsonData = JSON.parse(JSON.stringify(dbr));
	  //console.log("jsonData", jsonData);
	  console.log(dbr);
	  for(i=0;i<dbr.length;i++){
      dbr[i][1] = Number(dbr[i][1]);
    }
	  var data = google.visualization.arrayToDataTable(dbr,true); //false if there are headers
       var options = {
          title: 'Words',
          is3D: true,
        };
      // Instantiate and draw the chart.
      var chart = new google.visualization.PieChart(document.getElementById('myPieChart'));
      chart.draw(data, options);
      var chart = new google.visualization.ColumnChart(document.getElementById('myColumnChart'));
      chart.draw(data, options);
      var chart = new google.visualization.ScatterChart(document.getElementById('myScatterChart'));
      chart.draw(data, options);


    }
</script>
</head>
<body>
<!-- Identify where the chart should be drawn. -->
  <div id="myPieChart" style="width: 1400px; height: 500px;"> </div>
  <br>
  <div id="myColumnChart" style="width: 1400px; height: 500px;"> </div>
  <br>
  <div id="myScatterChart" style="width: 1400px; height: 500px;"> </div>
</body>
</html>