

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
var TOUCHINGROTATION = false;
var TOUCHINGTRANSLATION = false;

var r = 0;
var x = 0;
var y = 0;

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
		
		TOUCHINGROTATION = true;

		var touch;
		if (!TOUCHINGTRANSLATION) {
			touch = e.touches[0];
		} else {
			touch = e.touches[1];
		}


		var rect = rotationalControl.getBoundingClientRect();
		var y = touch.pageY - rect.top;
		var dir = FWD;
		var height = 400;
		var percentage = (y - (height/2)) / (height/2);

		// Update global
		r = percentage;
		drawRotationalControl();

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
	rotationalControl.addEventListener('touchend', function (e)  {
		TOUCHINGROTATION = false;
	}, false);

	// translational control	
	var translationalControl = document.getElementById("translationalControl");

	var translationHandler = function (e) {

		// Multiple touches
		TOUCHINGTRANSLATION = true;
		var touch;
		if (!TOUCHINGROTATION) {
			touch = e.touches[0];
		} else {
			touch = e.touches[1];
		}

		// No bounce
		e.preventDefault();

		var rect = translationalControl.getBoundingClientRect();
		var x = touch.pageX - rect.left;
		var y = touch.pageY - rect.top;
		var edge = 300;
		var _x = (x - (edge/2))/(edge/2);
		var _y = -1*(y - (edge/2))/(edge/2);

		// Update globals
		x = _x;
		y = _y;
		drawTranslationalControl(x, y);

		var xVal = (_x < 0) ? -1 * _x : _x;
		var yVal = (_y < 0) ? -1 * _y : _y;


		var xDir = FWD;
		if (_x < 0) { xDir = REV; }
		var yDir = FWD;
		if (_y < 0) { yDir = REV; }

		if ( lock === 0 ) {
			lock = 1;
			$.get('/motors?xVal=' + xVal + '&xDir=' + xDir + '&yVal=' + yVal + '&yDir=' + yDir,
			      function(data) { lock = 0; }
			     );
		}
	}

	translationalControl.addEventListener('touchstart', translationHandler, false);
	translationalControl.addEventListener('touchmove', translationHandler, false);
	translationalControl.addEventListener('touchend', function (e)  {
		TOUCHINGTRANSLATION = false;
	}, false);

});


var drawStopButton = function () {
	// Background
	var ctx = document.getElementById("stopButton").getContext("2d");
	ctx.beginPath();
	ctx.fillStyle = "#FF0000";
	var width = 300;
	var padding = 50;
	ctx.rect(padding, 30, 200, 100);
	ctx.fill();

	// Text
	ctx.fillStyle = "#000000";
	ctx.font="30px Verdana";
	ctx.fillText("STOP", 110, 90);
}

var deadZoneColor = "blue";
var activeZoneColor = "gray";
var positionIndicatorColor = "white";

var drawRotationalControl = function (_r) {	
	var rotational = document.getElementById("rotationalControl")
	var ctx = rotational.getContext("2d");

	var height = rotational.height;
	var width = rotational.width;
	ctx.clearRect (0, 0, width, height);
	
	ctx.beginPath();
	ctx.fillStyle = activeZoneColor;
	ctx.rect(0, 0, width, height * .4);
	ctx.fill();

	ctx.beginPath();
	ctx.fillStyle = deadZoneColor;
	ctx.rect(0,height * .4, width, height * .6);
	ctx.fill();

	ctx.beginPath();
	ctx.fillStyle = activeZoneColor;
	ctx.rect(0,height * .6, width, height);
	ctx.fill();

	ctx.beginPath();
	ctx.fillStyle = positionIndicatorColor;
	var pos = (height / 2) + (r * height / 2);
	ctx.lineWidth = 5;
	ctx.moveTo(0, pos);
	ctx.lineTo(width, pos);
    ctx.stroke();

}

var drawTranslationalControl = function (_x,_y) {
	var translational = document.getElementById("translationalControl")
	var ctx = translational.getContext("2d");

	var height = translational.height;
	var width = translational.width;

	ctx.beginPath();
	ctx.fillStyle =   activeZoneColor;
	ctx.rect(0,0,width * .4, height * .4);
	ctx.fill();

	ctx.beginPath();
	ctx.fillStyle =   activeZoneColor;
	ctx.rect(width * .6, 0, width *.4, height * .4);
	ctx.fill();

	ctx.beginPath();
	ctx.fillStyle =   activeZoneColor;
	ctx.rect(0, height * .6, width * .4, height * .4);
	ctx.fill();

	ctx.beginPath();
	ctx.fillStyle =   activeZoneColor;
	ctx.rect(width * .6, height * .6, width *.4, height * .4);
	ctx.fill();

	ctx.beginPath();
	ctx.fillStyle =   deadZoneColor;
	ctx.rect(width * .4, 0, width *.2, height);
	ctx.fill();

	ctx.beginPath();
	ctx.fillStyle =   deadZoneColor;
	ctx.rect(0, height * .4, width, height * .2);
	ctx.fill();

	// y
	ctx.beginPath();
	ctx.fillStyle = positionIndicatorColor;
	var yPos =  (height / 2) - (_y * height / 2);
	ctx.lineWidth = 5;
	ctx.moveTo(0, yPos);
	ctx.lineTo(width, yPos);
    ctx.stroke();

    // x
	ctx.beginPath();
	ctx.fillStyle = positionIndicatorColor;
	xPos =  (width / 2) + (_x * width / 2);
	ctx.lineWidth = 10;
	ctx.moveTo(xPos, 0);
	ctx.lineTo(xPos, height);
    ctx.stroke();
}

// draw ui when page is ready
$(function () {
	drawStopButton();
	drawRotationalControl(0);
	drawTranslationalControl(0,0);
});