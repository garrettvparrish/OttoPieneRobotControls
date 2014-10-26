

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

myLayout.registerComponent('graph', function(container, state) {

});


myLayout.registerComponent('motor1Graph', function (container, state) {

});

myLayout.registerComponent('rotationalVelocityGraph', function (container, state) {

});

myLayout.registerComponent('rotationalVelocityController', function (container, state) {

});

myLayout.registerComponent('motor2Graph', function (container, state) {

});

myLayout.registerComponent('horizontalVelocityGraph', function (container, state) {

});

myLayout.registerComponent('gyro', function (container, state) {

});

myLayout.registerComponent('motor3Graph', function (container, state) {

});

myLayout.registerComponent('verticalVelocityGraph', function (container, state) {

});

myLayout.registerComponent('translationalVelocityController', function (container, state) {

});


myLayout.init();