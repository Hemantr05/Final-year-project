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
//delete *from project; //Because we need to delete data from table for using next time.
?>;

console.log(typeof dbr);

google.charts.load('current', {packages: ['corechart']});
google.charts.load('current', {'packages':['table']});
    google.charts.setOnLoadCallback(drawChart);

    function drawChart() {
      // Define the chart to be drawn.
      
      
      //const jsonData = JSON.parse(JSON.stringify(dbr));
	  //console.log("jsonData", jsonData);
	  console.log(dbr);
	  for(i=0;i<dbr.length;i++){
      dbr[i][1] = Number(dbr[i][1]); //It's an array of two-columned arrays. 0th column is words and 1st column is number
    }
	  var data = google.visualization.arrayToDataTable(dbr,true); //false if there are headers
       var options = {
          title: 'Keywords',
          is3D: true,
        };
        var options1 = {
          title: 'Keywords',
          pieHole : 0.4,
        };
        var options2 = {
          title: 'Keywords',
          legend: 'none',
          pieSliceText: 'label',
          slices: {  4: {offset: 0.2},
                    12: {offset: 0.3},
                    14: {offset: 0.4},
                    15: {offset: 0.5},
                    50 :{offset: 0.6},
                    75 :{offset: 0.7},
                    100 :{offset: 0.5},
                    125 :{offset: 0.4},
                    150 :{offset: 0.6},
                    175 :{offset: 0.3},
                    200 :{offset: 0.6},
                    225 :{offset: 0.5},
          },
        };
        
      // Instantiate and draw the chart.
      var chart = new google.visualization.PieChart(document.getElementById('myPieChart'));
      chart.draw(data, options);
      var chart = new google.visualization.ColumnChart(document.getElementById('myColumnChart'));
      chart.draw(data, options);
      var chart = new google.visualization.ScatterChart(document.getElementById('myScatterChart'));
      chart.draw(data, options);
      var chart = new google.visualization.BarChart(document.getElementById('myBarChart'));
      chart.draw(data, options);
      var chart = new google.visualization.PieChart(document.getElementById('myDonutChart'));
      chart.draw(data, options1);
      var chart = new google.visualization.PieChart(document.getElementById('mySliceChart'));
      chart.draw(data, options2);
      var table = new google.visualization.Table(document.getElementById('table_div'));
	    table.draw(data, {showRowNumber: true, width: '100%', height: '100%'});


    }
</script>
</head>
<body>
<!-- Identify where the chart should be drawn. -->
  <div id="table_div" style="width: 700px; height: 500px;"> </div>
  <br>
  <div id="myPieChart" style="width: 1400px; height: 500px;"> </div>
  <br>
  <div id="myColumnChart" style="width: 1400px; height: 500px;"> </div>
  <br>
  <div id="myScatterChart" style="width: 1400px; height: 500px;"> </div>
  <br>
  <div id="myBarChart" style="width: 1400px; height: 500px;"> </div>
  <br>
  <div id="myDonutChart" style="width: 1400px; height: 500px;"> </div>
  <br>
  <div id="mySliceChart" style="width: 1400px; height: 500px;"> </div>
  <br>
  <br>
  
</body>
</html>