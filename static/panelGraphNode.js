var graphCount = 0

var PanelGraphNode = function() {

  this.initPanel = function(container, componentState) {

    // Create the graph
    var graph = document.createElement('div');
    graph.id = "graph-"+graphCount;
    graph.className = "graph-container";
    graphCount += 1;

    container.getElement()[0].appendChild(graph);

    // We use an inline data source in the example, usually data would
    // be fetched from a server

    var data = [],
      totalPoints = 300;

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

    // Set up the control widget
    var graphName = "#graph-"+graphCount;
    // var plot = $.plot(graphName, [ getRandomData() ], {
    //   series: {
    //     shadowSize: 0 // Drawing is faster without shadows
    //   },
    //   yaxis: {
    //     min: 0,
    //     max: 100
    //   },
    //   xaxis: {
    //     show: false
    //   }
    // });

    function update() {
      // plot.setData([getRandomData()]);
      // plot.draw();
      setTimeout(update, 1000);
    }

    update();
}