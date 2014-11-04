var socket = io.connect('http://' + document.domain + ':' + location.port);
socket.on('connect', function() {
    socket.emit('connect', {data: 'I\'m connected!   ' + myip});
});


// Graph displays
var motor1;
var motor2;
var motor3;
var rotationalVelocity = 0.0;
var horizontalVelocity = 0.0;
var verticalVelocity = 0.0;
var lastRotational = 0.0;
var lastHorizontal = 0.0;
var lastVertical = 0.0;

// Controllers
var rotationalVelocityController;
var translationalVelocityController;
var controllerWidth = 250.0;
var controllerHeightOffset = 50.0;
var controllerHeight = 250.0;
var translationalVelocityMappingCoefficient = controllerWidth/2.0;

// Current Values
var currentHorizontalVelocity;
var currentVerticalVelocity;
var currentRotationalVelocity;

// Counters
var count = 0;

var pi = Math.PI;

var init = function () {
	console.log("Initializing Data Stream");
	
	// Motors
	motor1 = document.getElementById("graph-0-value");
	motor2 = document.getElementById("graph-2-value");
	motor3 = document.getElementById("graph-4-value");

	// Velocities
	rotationalVelocity = document.getElementById("graph-1-value");
	horizontalVelocity = document.getElementById("graph-3-value");
	verticalVelocity = document.getElementById("graph-5-value");

	// Coordinate conversion function
	var canvasToRelativeCoordinates = function (controller, x, y) {
		var _x = controller.offsetLeft;
    	var _y = controller.offsetTop;

    	// map from -125 --> 125 in both directions
    	var relativeX = (x-_x) - controllerWidth/2.0;
    	var relativeY = -1*((y-_y) - controllerHeightOffset - controllerWidth/2.0);

    	return { 'x' : relativeX, 'y': relativeY };
	}

	// Controllers
	rotationalVelocityController = document.getElementById("rotationalVelocityController");
  	var rotationHandler = function (e) {
		var touch = e.touches[0]
		var coord = canvasToRelativeCoordinates(rotationalVelocityController, touch.pageX, touch.pageY)
		var x = coord['x'];
		var y = coord['y'];

		var theta = 0.0;

        if(x == 0 && y >= 0){
            theta = 0.0;
        }
        else if (x > 0 && y == 0){
            theta = pi / 2.0;
        }
        else if (x < 0 && y == 0){
            theta = pi / -2.0;
        }
        else if (x == 0 && y < 0){
            theta = pi;
        }
        else{
            theta = Math.atan2(x,y);
        }
        
        theta = theta / pi;  
        
		console.log("Rotational: Theta " + theta);
		updateRotationalVelocity(theta.toFixed(2));
		
		// Submit all values
		updateValues();
	}

	rotationalVelocityController.addEventListener('touchmove', rotationHandler, false);
	rotationalVelocityController.addEventListener('touchstart', rotationHandler, false);

	rotationalVelocityController.addEventListener('touchend', function (e) {
		updateRotationalVelocity(0.0);
		updateValues();
	});

	translationalVelocityController = document.getElementById("translationalVelocityController");
	
	var translationHandler = function (e) {
		var touch = e.touches[0]
		var coord = canvasToRelativeCoordinates(translationalVelocityController, touch.pageX, touch.pageY)
		var x = coord['x'] / translationalVelocityMappingCoefficient;
		var y = coord['y'] / translationalVelocityMappingCoefficient;
        
        if (x > 1){
            x = 1
        }
        else if(x < -1){
            x = -1
        }
        
        if (y > 1){
            y = 1
        }
        else if (y < -1){
            y = -1
        }

		console.log("Translational: X: " + x + " Y: " + y);

		// Update displays for velocities
		updateHorizontalVelocity(x.toFixed(2));
		updateVerticalVelocity(y.toFixed(2));

		// Submit all values
		updateValues();
	}
	translationalVelocityController.addEventListener('touchmove', translationHandler, false);
	translationalVelocityController.addEventListener('touchstart', translationHandler, false);

	translationalVelocityController.addEventListener('touchend', function (e) {
		updateHorizontalVelocity(0.0);
		updateVerticalVelocity(0.0);
		updateValues();
	});

	// Disable bounce scrolling on controller web page
	document.ontouchmove = function(event){
	    event.preventDefault();
	}
}

// Submit Translate values to server
var updateValues = function () {
    var controlString = lastHorizontal + ',' + lastVertical + ',' + lastRotational;
    console.log("sent control string: " + controlString);
    socket.emit('control',{data: controlString});
    //socket.emit('x',{data: lastHorizontal});
    //socket.emit('y',{data: lastVertical});
    //socket.emit('r',{data: lastRotational});
}



 //Update methods
socket.on('motor1',function (value) {
	motor1.innerHTML = value;
});

socket.on('motor2',function (value) {
	motor2.innerHTML = value;
});

socket.on('motor3',function (value) {
	motor3.innerHTML = value;
});

var updateRotationalVelocity = function (value) {
	rotationalVelocity.innerHTML = value;
	currentRotationalVelocity = value;
    lastRotational = value;
	// do calculations for all the other ones
}

var updateHorizontalVelocity = function (value) {
	horizontalVelocity.innerHTML = value;
	currentHorizontalVelocity = value;
    lastHorizontal = value;
	// do calculations for all others
}

var updateVerticalVelocity = function (value) {
	verticalVelocity.innerHTML = value;
	currentVerticalVelocity = value;
    lastVertical = value;
}

setTimeout(init, 1000);

