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
	                height: 100
	            },{
	                type: 'component',
	                componentName: 'rotationalVelocityGraph',
	                height: 100
	            },{
	                type: 'component',
	                componentName: 'rotationalVelocityController',
	                height: 100
	            }
            ]
        }, {
            type: 'column',
            width: 60,
            content: [
            	{
	                type: 'component',
	                componentName: 'motor2Graph',
	                height: 100
	            },{
	                type: 'component',
	                componentName: 'horizontalVelocityGraph',
	                height: 100
	            },{
	                type: 'component',
	                componentName: 'gyro',
	                height: 100
	            }
            ]

        },{
            type: 'column',
            width: 60,
            content: [
            	{
	                type: 'component',
	                componentName: 'motor3Graph',
	                height: 100
	            },{
	                type: 'component',
	                componentName: 'verticalVelocityGraph',
	                height: 100
	            },{
	                type: 'component',
	                componentName: 'translationalVelocityController',
	                height: 100
	            }
            ]

        }]
    }]
};

var myLayout = new GoldenLayout(config);

var graphNode = new PanelGraphNode();

myLayout.registerComponent('motor1Graph', graphNode.initPanel);
myLayout.registerComponent('motor2Graph', graphNode.initPanel);
myLayout.registerComponent('motor3Graph', graphNode.initPanel);

myLayout.registerComponent('rotationalVelocityGraph', graphNode.initPanel);
myLayout.registerComponent('horizontalVelocityGraph', graphNode.initPanel);
myLayout.registerComponent('verticalVelocityGraph', graphNode.initPanel);

myLayout.registerComponent('rotationalVelocityController', function (container, componentState) {
	container.getElement().html( '<h2 class="label">' + "ROTATIONAL VELOCITY" + '</h2>' );
});

myLayout.registerComponent('gyro', function (container, componentState) {
	
});


myLayout.registerComponent('translationalVelocityController', function (container, componentState) {
	
});

myLayout.init();