var motor1;
var motor2;
var motor3;
var rotationalVelocity;
var horizontalVelocity;
var verticalVelocity;

var count = 0;

var init = function () {
	console.log("Initializing Data Stream");
	motor1 = document.getElementById("graph-0-value");
	motor2 = document.getElementById("graph-1-value");
	motor3 = document.getElementById("graph-2-value");

	rotationalVelocity = document.getElementById("graph-3-value");
	horizontalVelocity = document.getElementById("graph-4-value");
	verticalVelocity = document.getElementById("graph-5-value");
	console.log(motor1);

	setInterval(function () {
		count += 1;

		updateMotor1Value(count);
		updateMotor2Value(count);
		updateMotor3Value(count);
		updateRotationalVelocity(count);
		updateHorizontalVelocity(count);
		updateVerticalVelocity(count);

		console.log(count);

	}, 1000);
}

var updateMotor1Value = function (value) {
	motor1.innerHTML = value;
}

var updateMotor2Value = function (value) {
	motor2.innerHTML = value;
}

var updateMotor3Value = function (value) {
	motor3.innerHTML = value;
}

var updateRotationalVelocity = function (value) {
	rotationalVelocity.innerHTML = value;
}

var updateHorizontalVelocity = function (value) {
	horizontalVelocity.innerHTML = value;
}

var updateVerticalVelocity = function (value) {
	verticalVelocity.innerHTML = value;
}

setTimeout(init, 1000);