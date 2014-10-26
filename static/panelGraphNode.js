var graphCount = 0

var PanelGraphNode = function() {

  this.initPanel = function(container, componentState) {

    // TODO: NEED TO FIX THIS SO IT OUTPUTS A GRAPH --> NOT HARD ONCE IT WORKS --> JUST GET VALUE FOR NOW

    var graphValue = document.createElement('div');
    graphValue.id = "graph-" + graphCount + "-value";
    graphValue.class = "graph-value";
    graphValue.style.width = "100px";
    graphValue.style.height = "100px";

    // Create a title for the graph
    var title = "";
    switch (graphCount) {
      // Motor 1
      case 0:
        title = "MOTOR 1"
        break;

      // Motor 2
      case 1:
        title = "ROTATIONAL VELOCITY"
        break;

      // Motor 3
      case 2:
        title = "MOTOR 2"
        break;

      // Rotational Velocity Graph
      case 3:
        title = "HORIZONTAL VELOCITY"
        break;

      // Horizontal Velocity Graph
      case 4:
        title = "MOTOR 3"
        break;

      // Vertical Velocity Graph
      case 5:
        title = "VERTICAL VELOCITY"
        break;

      default:
        break;
    } 
    var heading = '<h2 class="label">' + title + '</h2>';
    var value = '<h2 id="' + graphValue.id + '" class="graphValue">' + 0.0 + '</h2>'
    container.getElement().html(heading + value);

    // Update graph count
    console.log("Created Graph" + graphValue.id);
    console.log(title)
    graphCount += 1;
  }
}