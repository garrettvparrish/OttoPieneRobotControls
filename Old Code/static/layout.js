var config = {
    settings: {hasHeaders:false},
    dimensions: {borderWidth:2},
    content: [{
        type: 'row',
        content: [{
            type: 'column',
            width: 60,
            content: [{
	                type: 'component',
	                componentName: 'rotationalVelocityGraph',
	                height: 80
	            },{
	                type: 'component',
	                componentName: 'rotationalVelocityController',
	                height: 140
	            }
            ]
        }, {
            type: 'column',
            width: 60,
            content: [
            	{
	                type: 'component',
	                componentName: 'horizontalVelocityGraph',
	                height: 80
	            },{
	                type: 'component',
	                componentName: 'gyro',
	                height: 140
	            }
            ]

        },{
            type: 'column',
            width: 60,
            content: [
            	{
	                type: 'component',
	                componentName: 'verticalVelocityGraph',
	                height: 80
	            },{
	                type: 'component',
	                componentName: 'translationalVelocityController',
	                height: 140
	            }
            ]
        }]
    }]
};

console.log("Creating Layout.");

var myLayout = new GoldenLayout(config);

var graphNode = new PanelGraphNode();

myLayout.registerComponent('motor1Graph', graphNode.initPanel);
myLayout.registerComponent('rotationalVelocityGraph', graphNode.initPanel);
myLayout.registerComponent('rotationalVelocityController', function (container, componentState) {
	var label =  '<h2 class="label">' + "ROTATIONAL VELOCITY CONTROL" + '</h2>';
	var canvas = '<center><canvas id="rotationalVelocityController"></canvas></center>' 
	container.getElement().html(label + canvas);
});


myLayout.registerComponent('motor2Graph', graphNode.initPanel);
myLayout.registerComponent('horizontalVelocityGraph', graphNode.initPanel);
myLayout.registerComponent('gyro', function (container, componentState) {
	var label = '<h2 class="label">' + "GYRO" + '</h2>';
	container.getElement().html(label);

   	// // Robot class
    // 	function Robot(context) {
    // 		console.log("Created new robot.");
    // 		this.ctx = context
    // 		this.position = new Location(100.0, 100.0);

    // 		// calculated in degrees
    // 		this.rotationAngle = 0.0;

    // 		this.updatePosition = function (x,y){
    // 			this.position = new Location(x,y);
    // 			this.draw();
    // 		}

    // 		this.updateAngle = function(angle) {
    // 			this.rotationAngle = angle;
    // 			this.draw();
    // 		}

	   //  	this.rotate = function(x,y, th) {
				// x1 = x*cos(th) - y*sin(th)
				// y1 = x*sin(th) + y*cos(th)
	   //  		return (x, y)
	   //  	}

    // 		this.draw = function () {
    // 			this.ctx.clearRect(0, 0, canvas.width, canvas.height);
    // 			var a = 9.5 * scale / 2.0;
    // 			var r = 12.5 * scale;
    // 			var b = 17.0 * scale;
    // 			var sin30 = .5;
    // 			var cos60 = sin30;
    // 			var sin60 = 0.86;
    // 			var cos30 = sin60;
    // 			var x = this.position.x;
    // 			var y = this.position.y;
    // 			var theta = this.rotationAngle; 

    // 			this.ctx.beginPath();

    // 			(x1, y1) = this.rotate(-a, -r, theta);
				// this.ctx.moveTo(x + x1, y + y1);
				
    // 			(x1, y1) = this.rotate(a, -r, theta);
				// this.ctx.lineTo(x + x1, y + y1);
				
				// (x1, y1) = this.rotate(r*cos30 + a*sin30, r*sin30 - a*cos30, theta);
				// this.ctx.lineTo(x + x1, y + y1);
				
				// (x1, y1) = this.rotate(b/2, r*sin30 + a*cos30, theta);
				// this.ctx.lineTo(x + x1, y + y1);
				
				// (x1, y1) = this.rotate(-b/2, r*sin30 + a*cos30, theta);
				// this.ctx.lineTo(x + x1, y + y1);
				
				// (x1, y1) = this.rotate(- r*cos30 - a*sin30,  r*sin30 - a*cos30, theta);
				// this.ctx.lineTo(x + x1, y + y1);
				
				// (x1, y1) = this.rotate(-a, -r, theta);
				// this.ctx.lineTo(x + x1, y + y1);
				
				// this.ctx.fill();
    // 		}
    // 	}

    // robot = new Robot(ctx);
    // robot.draw();

});

myLayout.registerComponent('motor3Graph', graphNode.initPanel);
myLayout.registerComponent('verticalVelocityGraph', graphNode.initPanel);
myLayout.registerComponent('translationalVelocityController', function (container, componentState) {
	var label = '<h2 class="label">' + "TRANSLATIONAL VELOCITY CONTROL" + '</h2>';
	var canvas = '<center><canvas id="translationalVelocityController"></canvas></center>' 
	container.getElement().html(label + canvas);
});

myLayout.init();



