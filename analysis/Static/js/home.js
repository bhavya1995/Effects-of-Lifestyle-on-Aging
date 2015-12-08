window.onload = function (){
	main();
}

function main(){
	clickCount = 0
	$(document).ready(function() {
	    $('select').material_select();
	  });
	$('.predictOutcomeParent').css('display', 'none')
	$('#container3').css('display', 'none')
	$('#prev').css('display', 'none')
	$('#next').css('display', 'block')

	$('.predict').click(function(){
		$.ajax({
			type: 'GET',
			data: {
				'patientId': $('#patientID').val(),
				'type': $('#typePredict').val()
			},
			url: '/predictPatient',
			success: function(data){
				console.log(data)
				$('.predictOutcomeParent').css('display', 'block')
				$('.predictionOutcome').text(data['data'])
			}
		})
	})

	$.ajax({
		type: 'GET',
		url: '/getKmeans',
		success: function(data){
			console.log(data)
		    $('#container').highcharts({
		        chart: {
		            type: 'column'
		        },
		        title: {
		            text: 'Effects of Lifestyle on Aging'
		        },
		        subtitle: {
		            text: 'K Means Algorithm'
		        },
		        xAxis: {
		            categories: [
		                'Cluster 1',
		                'Cluster 2',
		                'Cluster 3',
		                'Cluster 4',
		                'Cluster 5',
		                'Cluster 6',
		                'Cluster 7',
		                'Cluster 8',
		            ],
		            crosshair: true
		        },
		        yAxis: {
		            min: 0,
		            title: {
		                text: 'Accuracy (%)'
		            }
		        },
		        tooltip: {
		            headerFormat: '<span style="font-size:10px">{point.key}</span><table>',
		            pointFormat: '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' +
		                '<td style="padding:0"><b>{point.y:.1f} %</b></td></tr>',
		            footerFormat: '</table>',
		            shared: true,
		            useHTML: true
		        },
		        plotOptions: {
		            column: {
		                pointPadding: 0.2,
		                borderWidth: 0
		            }
		        },
		        series: [{
		            name: 'All 256 Parameters are taken into consideration',
		            data: data['all col'],
		         	color: '#b71c1c'
		        }]
		    });

	$('.btn-1').click(function(){
		if ($(this).attr('id') == 'prev'){
			clickCount -= 1
		}
		else {
			clickCount += 1
		}
		if (clickCount == 0){
			$('#prev').css('display', 'none')
			$('#next').css('display', 'block')
			$('#container1').css('display', 'none')
			$('#container').css('display', 'block')

		}
		else if (clickCount == 8){
			$('#prev').css('display', 'block')
			$('#next').css('display', 'none')
		}
		else {
			$('#prev').css('display', 'block')
			$('#next').css('display', 'block')			
		}

		if (clickCount === 1){
			$('#container').css('display', 'none')
			$('#container10').css('display', 'none')
			$('#container1').css('display', 'block')
		    $('#container1').highcharts({
		        chart: {
		            type: 'pie',
		            options3d: {
		                enabled: true,
		                alpha: 45,
		                beta: 0
		            }
		        },
		        title: {
		            text: 'Clusters Size Distribution in Pie Chart'
		        },
		        tooltip: {
		            pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
		        },
		        plotOptions: {
		            pie: {
		                allowPointSelect: true,
		                cursor: 'pointer',
		                depth: 35,
		                dataLabels: {
		                    enabled: true,
		                    format: '{point.name}'
		                }
		            }
		        },
		        series: [{
		            type: 'pie',
		            name: 'Clusters Share',
		            data: [
		                {
		                    name: 'Cluster 0',
		                    y: 7029,
		                    sliced: true,
		                    selected: true
		                },
		                ['Cluster 1', 504.0],
		                ['Cluster 2', 522.0],
		                ['Cluster 3', 70],
		                ['Cluster 4', 1698],
		                ['Cluster 5', 264],
		                ['Cluster 6', 265],
		                ['Cluster 7', 68],

		            ]
		        }]
		    });

		}
		if (clickCount == 2){
			$('#container1').css('display', 'none')
			$('#container10').css('display', 'block')
			$('#container11').css('display', 'none')

		    $('#container10').highcharts({
		        chart: {
		            type: 'column'
		        },
		        title: {
		            text: 'Effects of Lifestyle on Aging'
		        },
		        subtitle: {
		            text: 'K Means Algorithm'
		        },
		        xAxis: {
		            categories: [
		                'Cluster 1',
		                'Cluster 2',
		                'Cluster 3',
		                'Cluster 4',
		                'Cluster 5',
		                'Cluster 6',
		                'Cluster 7',
		                'Cluster 8',
		            ],
		            crosshair: true
		        },
		        yAxis: {
		            min: 0,
		            title: {
		                text: 'Accuracy (%)'
		            }
		        },
		        tooltip: {
		            headerFormat: '<span style="font-size:10px">{point.key}</span><table>',
		            pointFormat: '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' +
		                '<td style="padding:0"><b>{point.y:.1f} %</b></td></tr>',
		            footerFormat: '</table>',
		            shared: true,
		            useHTML: true
		        },
		        plotOptions: {
		            column: {
		                pointPadding: 0.2,
		                borderWidth: 0
		            }
		        },
		        series: [{
		            name: 'Random one third of Parameters are taken into consideration',
		            data: data['random one third'],
		         	color: '#004d40'
		        }]
		    });			
		}
		if (clickCount == 3){
			$('#container10').css('display', 'none')
			$('#container11').css('display', 'block')
			$('#container12').css('display', 'none')

		    $('#container11').highcharts({
		        chart: {
		            type: 'column'
		        },
		        title: {
		            text: 'Effects of Lifestyle on Aging'
		        },
		        subtitle: {
		            text: 'K Means Algorithm'
		        },
		        xAxis: {
		            categories: [
		                'Cluster 1',
		                'Cluster 2',
		                'Cluster 3',
		                'Cluster 4',
		                'Cluster 5',
		                'Cluster 6',
		                'Cluster 7',
		                'Cluster 8',
		            ],
		            crosshair: true
		        },
		        yAxis: {
		            min: 0,
		            title: {
		                text: 'Accuracy (%)'
		            }
		        },
		        tooltip: {
		            headerFormat: '<span style="font-size:10px">{point.key}</span><table>',
		            pointFormat: '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' +
		                '<td style="padding:0"><b>{point.y:.1f} %</b></td></tr>',
		            footerFormat: '</table>',
		            shared: true,
		            useHTML: true
		        },
		        plotOptions: {
		            column: {
		                pointPadding: 0.2,
		                borderWidth: 0
		            }
		        },
		        series: [{
		            name: 'Only First one third columns are taken into consideration',
		            data: data['first one third'],
		         	color: '#e65100'
		        }]
		    });			

		}
		if (clickCount == 4){
			$('#container11').css('display', 'none')
			$('#container12').css('display', 'block')
			$('#container13').css('display', 'none')

		    $('#container12').highcharts({
		        chart: {
		            type: 'column'
		        },
		        title: {
		            text: 'Effects of Lifestyle on Aging'
		        },
		        subtitle: {
		            text: 'K Means Algorithm'
		        },
		        xAxis: {
		            categories: [
		                'Cluster 1',
		                'Cluster 2',
		                'Cluster 3',
		                'Cluster 4',
		                'Cluster 5',
		                'Cluster 6',
		                'Cluster 7',
		                'Cluster 8',
		            ],
		            crosshair: true
		        },
		        yAxis: {
		            min: 0,
		            title: {
		                text: 'Accuracy (%)'
		            }
		        },
		        tooltip: {
		            headerFormat: '<span style="font-size:10px">{point.key}</span><table>',
		            pointFormat: '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' +
		                '<td style="padding:0"><b>{point.y:.1f} %</b></td></tr>',
		            footerFormat: '</table>',
		            shared: true,
		            useHTML: true
		        },
		        plotOptions: {
		            column: {
		                pointPadding: 0.2,
		                borderWidth: 0
		            }
		        },
		        series: [{
		            name: 'Second one third is taken into consideration',
		            data: data['second one third'],
		         	color: '#3e2723'
		        }]
		    });			

		}
		if (clickCount == 5){
			$('#container12').css('display', 'none')
			$('#container2').css('display', 'none')
			$('#container13').css('display', 'block')

		    $('#container13').highcharts({
		        chart: {
		            type: 'column'
		        },
		        title: {
		            text: 'Effects of Lifestyle on Aging'
		        },
		        subtitle: {
		            text: 'K Means Algorithm'
		        },
		        xAxis: {
		            categories: [
		                'Cluster 1',
		                'Cluster 2',
		                'Cluster 3',
		                'Cluster 4',
		                'Cluster 5',
		                'Cluster 6',
		                'Cluster 7',
		                'Cluster 8',
		            ],
		            crosshair: true
		        },
		        yAxis: {
		            min: 0,
		            title: {
		                text: 'Accuracy (%)'
		            }
		        },
		        tooltip: {
		            headerFormat: '<span style="font-size:10px">{point.key}</span><table>',
		            pointFormat: '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' +
		                '<td style="padding:0"><b>{point.y:.1f} %</b></td></tr>',
		            footerFormat: '</table>',
		            shared: true,
		            useHTML: true
		        },
		        plotOptions: {
		            column: {
		                pointPadding: 0.2,
		                borderWidth: 0
		            }
		        },
		        series: [{
		            name: 'Last Remaining one third are taken into consideration',
		            data: data['last remaining'],
		         	color: '#263238'
		        }]
		    });			

		}
		if (clickCount === 6){
			$('#container13').css('display', 'none')
			$('#container2').css('display', 'block')
			$('#container3').css('display', 'none')
			$('.predictOutcomeParent').css('display', 'none')

		    $('#container2').highcharts({
		        chart: {
		            type: 'column'
		        },
		        title: {
		            text: 'Effects of Lifestyle on Aging'
		        },
		        subtitle: {
		            text: 'K Means Algorithm'
		        },
		        xAxis: {
		            categories: [
		                'Cluster 1',
		                'Cluster 2',
		                'Cluster 3',
		                'Cluster 4',
		                'Cluster 5',
		                'Cluster 6',
		                'Cluster 7',
		                'Cluster 8',
		            ],
		            crosshair: true
		        },
		        yAxis: {
		            min: 0,
		            title: {
		                text: 'Accuracy (%)'
		            }
		        },
		        tooltip: {
		            headerFormat: '<span style="font-size:10px">{point.key}</span><table>',
		            pointFormat: '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' +
		                '<td style="padding:0"><b>{point.y:.1f} %</b></td></tr>',
		            footerFormat: '</table>',
		            shared: true,
		            useHTML: true
		        },
		        plotOptions: {
		            column: {
		                pointPadding: 0.2,
		                borderWidth: 0
		            }
		        },
		        series: [{
		            name: 'All Columns',
		            data: data['all col'],
		            color:'#263238'

		        },{
		            name: 'Random one third',
		            data: data['random one third']

		        },{
		            name: 'First one third',
		            data: data['first one third'],
		            color: '#b71c1c'
		        },{
		            name: 'Second one third',
		            data: data['second one third']
		        },{
		            name: 'Last Remaining',
		            data: data['last remaining']

		        }]
		    });
		}	
		if (clickCount == 7){
			$('#container2').css('display', 'none')
			$('#container3').css('display', 'block')
			$('#container21').css('display', 'none')

		}
		if (clickCount == 8){
			$('#container3').css('display', 'none')
			$('.predictOutcomeParent').css('display', 'none')
			$('#container21').css('display', 'block')

		    $('#container21').highcharts({
		        chart: {
		            type: 'column'
		        },
		        title: {
		            text: 'Effects of Lifestyle on Aging'
		        },
		        subtitle: {
		            text: 'K Nearest Neighbour Algorithm'
		        },
		        xAxis: {
		            categories: [
		                'All Parameters',
		                'Only Large Parameters',
		                'All Parameters except Large Parameters'
		            ],
		            crosshair: true
		        },
		        yAxis: {
		            min: 0,
		            title: {
		                text: 'Accuracy (%)'
		            }
		        },
		        tooltip: {
		            headerFormat: '<span style="font-size:10px">{point.key}</span><table>',
		            pointFormat: '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' +
		                '<td style="padding:0"><b>{point.y:.1f} %</b></td></tr>',
		            footerFormat: '</table>',
		            shared: true,
		            useHTML: true
		        },
		        plotOptions: {
		            column: {
		                pointPadding: 0.2,
		                borderWidth: 0
		            }
		        },
		        series: [{
		            name: 'Accuracy',
		            data: [67.04, 67.08, 67.08],
		       		color: '#009688'
		        }]
		    });

		}		



		// }
	});

		}
	})























}