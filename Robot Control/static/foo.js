

// lock keeps requests from piling on top of each other.
// without this, you can get requests totally out of order

var lock = 0;

function mouseMove(event) {
    var speed = event.pageY / 4; // Just a hack to make the control box bigger
    if ( lock === 0 ) {
		lock = 1;
		$.get('/motors?m1s=' + speed + '&m2s=' + speed +'&m3s=' + speed,
		      function(data) {
			  $('#rotationalContro').html(data);
			  lock = 0;
		      }
		     );
    }
}

var FWD = 0;
var REV = 1;

// DIR: 0 = FWD, 1 = REV

// HANDLERS
$(document).ready(function() {

    // stop button
  	var stopHandler = function (e) { 
		console.log("STOP");

		if ( lock === 0 ) {
			lock = 1;
			$.get('/motorstop', function(data) { lock = 0; } );   
	    }
  	}

    var stopButton = document.getElementById("stopButton");
	stopButton.addEventListener('touchstart', stopHandler, false);

	// rotational control
	var rotationalControl = document.getElementById("rotationalControl");

	var rotationHandler = function (e) {
		// No bounce
		e.preventDefault();

		var touch = e.touches[0];
		var rect = rotationalControl.getBoundingClientRect();
		var y = touch.pageY - rect.top;
		var dir = FWD;
		var height = 550;
		var percentage = (y - (height/2)) / (height/2);
		if (percentage < 0) { 
			percentage = -1*percentage;
			dir = REV;
		}
		if ( lock === 0 ) {
			lock = 1;
			$.get('/motors?rVal=' + percentage + '&rDir=' + dir,
			      function(data) { lock = 0; }
			     );
		}
	}

	rotationalControl.addEventListener('touchstart', rotationHandler, false);
	rotationalControl.addEventListener('touchmove', rotationHandler, false);

	// translational control	
	var translationalControl = document.getElementById("translationalControl");

	var translationHandler = function (e) {
		// No bounce
		e.preventDefault();

		var touch = e.touches[0];
		var rect = translationalControl.getBoundingClientRect();
		var x = touch.pageX - rect.left;
		var y = touch.pageY - rect.top;
		var edge = 300;
		var _x = (x - (edge/2))/(edge/2);
		var _y = -1*(y - (edge/2))/(edge/2);
		console.log("TRANSLATION: " + _x + "," + _y);
	}

	translationalControl.addEventListener('touchstart', translationHandler, false);
	translationalControl.addEventListener('touchmove', translationHandler, false);

});

// draw ui when page is ready
$(function () {
	// STOP BUTTON

	// Background
	var ctx = document.getElementById("stopButton").getContext("2d");
	ctx.fillStyle = "#FF0000";
	var width = 300;
	var padding = 50;
	ctx.rect(padding, 30, 200, 100);
	ctx.fill();

	// Text
	ctx.fillStyle = "#000000";
	ctx.font="30px Verdana";
	ctx.fillText("STOP", 110, 90);
});