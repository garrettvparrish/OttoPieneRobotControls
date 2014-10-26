console.log("layout");

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
	                componentName: 'graph',
	                height: 100
	            },{
	                type: 'component',
	                componentName: 'graph',
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
	                componentName: 'graph',
	                height: 100
	            },{
	                type: 'component',
	                componentName: 'graph',
	                height: 100
	            }
            ]

        },{
            type: 'column',
            width: 60,
            content: [
            	{
	                type: 'component',
	                componentName: 'graph',
	                height: 100
	            },{
	                type: 'component',
	                componentName: 'graph',
	                height: 100
	            },{
	                type: 'component',
	                componentName: 'graph',
	                height: 100
	            }
            ]

        }]
    }]
};

var myLayout = new GoldenLayout(config);

myLayout.registerComponent('graph', function(container, state) {

});

myLayout.init();