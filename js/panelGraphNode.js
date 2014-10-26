var graphCount = 0

var PanelGraphNode = function() {

  this.initPanel = function(container, componentState) {

    var that = this;
    var data = [];
    var pdiv = null;
    var maximum = null;
    var plot = null;

    var nodeGraphContainer = document.createElement('div');

    // where the id of the graph node is created
    nodeGraphContainer.id = "hp-graph-"+graphCount;
    nodeGraphContainer.className = "hp-graph-container";
    graphCount += 1;

    container.getElement()[0].appendChild(nodeGraphContainer);

    var memory = [];

    // Graph update listener
    ipc.on('graph-post', function (refcon) {
      var number = parseInt(refcon["graph-number"]) - 1;

      if (parseInt(nodeGraphContainer.id.slice(-1)) == number) {
        var data = refcon["data"];
        var scaledData = (data * 50) + 50;

        memory.push([memory.length,scaledData]);

        var output = []
        if (memory.length > 298) {
          for (var i = 0; i < 299; ++i) {
            output.push([i, memory[i+1][1]]);
          }
          output.push([299, scaledData]);
          memory = output;
        }         

        plot.setData([memory]);        
        plot.draw();        
      }
    });

    var data = [],
          totalPoints = 300;

    var getData = function () {
      if (data.length > 0)
        data = data.slice(1);

      // Do a random walk

      while (data.length < totalPoints) {

        var prev = data.length > 0 ? data[data.length - 1] : 50,
          y = prev + Math.random() * 10 - 5;

        if (y < 0) {
          y = 0;
        } else if (y > 100) {
          y = 100;
        }

        data.push(y);
      }

      // Zip the generated y values with the x values

      var res = [];
      for (var i = 0; i < data.length; ++i) {
        res.push([i, data[i]])
      }

      return res;
    }

    var initGraph = function() {
      pdiv = $(nodeGraphContainer);
      maximum = pdiv.outerWidth() / 2 || 300;

      var series = [{
        data: getData(),
        lines: {
          fill: true
        }
      }];

      plot = $.plot(pdiv, series, {
        grid: {
          borderWidth: 1,
          minBorderMargin: 20,
          labelMargin: 10,
          backgroundColor: {
            colors: ["#222", "#222"]
          },
          margin: {
            top: 8,
            bottom: 20,
            left: 20
          },
          markings: function(axes) {
            var markings = [];
            var xaxis = axes.xaxis;
            for (var x = Math.floor(xaxis.min); x < xaxis.max; x += xaxis.tickSize * 2) {
              markings.push({ xaxis: { from: x, to: x + xaxis.tickSize }, color: "rgba(35, 35, 38, 0.2)" });
            }
            return markings;
          }
        },
        xaxis: {
          tickFormatter: function() {
            return "";
          }
        },
        yaxis: {
          min: 0,
          max: 110
        },
        legend: {
          show: false
        }
      });
    };

    setTimeout(initGraph, 1000);
  }
}

module.exports = PanelGraphNode;



