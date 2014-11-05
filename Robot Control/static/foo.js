

// lock keeps requests from piling on top of each other.
// without this, you can get requests totally out of order

var lock = 0;
function mouseMove(event) {
    var speed = event.pageY / 4; // Just a hack to make the control box bigger
    if ( lock === 0 ) {
	lock = 1;
	$.get('/motors?m1s=' + speed + '&m2s=' + speed +'&m3s=' + speed,
	      function(data) {
		  $('#control').html(data);
		  lock = 0;
	      }
	     );
    }
}

$(document).ready(function() {
    $('#control').mousemove(mouseMove);
});
