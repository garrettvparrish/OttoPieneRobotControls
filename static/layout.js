var config = {
    settings: {hasHeaders:false},
    dimensions: {borderWidth:2},
    content: [{
        type: 'row',
        content: [{
            type: 'column',
            width: 60,
            content: [
            	{
	                type: 'component',
	                componentName: 'motor1Graph',
	                height: 80
	            },{
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
	                componentName: 'motor2Graph',
	                height: 80
	            },{
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
	                componentName: 'motor3Graph',
	                height: 80
	            },{
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
});


myLayout.registerComponent('motor3Graph', graphNode.initPanel);
myLayout.registerComponent('verticalVelocityGraph', graphNode.initPanel);
myLayout.registerComponent('translationalVelocityController', function (container, componentState) {
	var label = '<h2 class="label">' + "TRANSLATIONAL VELOCITY CONTROL" + '</h2>';
	var canvas = '<center><canvas id="translationalVelocityController"></canvas></center>' 
	container.getElement().html(label + canvas);
});

myLayout.init();
