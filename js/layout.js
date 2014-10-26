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
			                componentName: 'graph',
			                height: 100
			            },{
			                type: 'component',
			                componentName: 'graph',
			                height: 100
			            },{
			                type: 'component',
			                componentName: 'rotationalVelocity',
			                height: 100
			            }
		            ]
		        }, {
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
			                componentName: 'graph',
			                height: 100
			            },{
			                type: 'component',
			                componentName: 'graph',
			                height: 100
			            },{
			                type: 'component',
			                componentName: 'translationalVelocity',
			                height: 100
			            }
		            ]

		        }]
		    }]
		};

		var myLayout = new GoldenLayout(config);

                var graphNode = new PanelGraphNode();
                myLayout.registerComponent('graph', graphNode.initPanel);

		myLayout.registerComponent('translationalVelocity', function (container, componentState) {

		});

		myLayout.registerComponent('rotationalVelocity', function (container, componentState) {

		});

		myLayout.registerComponent('gyro', function (container, componentState) {

		});

		myLayout.init();