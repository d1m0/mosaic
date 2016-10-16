
(function () {

  var drawChart = function() {
    var tl = document.getElementById('timeline')
    var underlyingData = tl._data; // must be set by template file
    var data = google.visualization.arrayToDataTable(underlyingData);

    var options = {
      // title: 'Company Performance',
      curveType: 'function',
      legend: { position: 'none' },
      hAxis: {showTextEvery: 2}
    };

    var chart = new google.visualization.LineChart(document.getElementById('timeline'));

    chart.draw(data, options);
  };

  google.charts.load('current', {'packages':['corechart']});
  google.charts.setOnLoadCallback(drawChart);



})();
