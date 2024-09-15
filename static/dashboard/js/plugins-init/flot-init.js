(function($) {
    "use strict"

	var plotData = [];
            for (var i = 0; i < x_data.length; i++) {
                plotData.push([i, y_data[i]]); // Use index + 1 for x-axis 
            }
	$.plot("#flotBar1", [{
		data: plotData
	}], {
		series: {
			bars: {
				show: true,
				lineWidth: 0,
				fillColor: '#105e95',
				barWidth: 0.95,
				align: 'center'
			}
		},
		grid: {
			borderWidth: 1,
			backgroundColor: { colors: ["#fff", "#eee"] },
			hoverable: true, // Enable hover events
            clickable: true,  // Enable click events
			borderColor: 'transparent'
		},
		yaxis: {
			tickColor: 'transparent',
			font: {
				color: '#000',
				size: 10
			},
		},
		xaxis: {
			tickColor: 'transparent',
			font: {
				color: '#000',
				size: 10
			},
			ticks: plotData.map((d, i) => [i, x_data[i]])
			// ticks: [[1, '1'], [2, '2'], [3, '3'],[4, '4'],[5, '5'], [6, '6'],[7, '7'], [8, '8'],[9, '9'], [10, '10'],[11,'11'], [12, '12']]
		},
	});

	$.plot("#flotBar2", [{
		data: [[0, 3], [2, 8], [4, 5], [6, 13], [8, 5], [10, 7], [12, 8], [14, 10]],
		bars: {
			show: true,
			lineWidth: 0,
			fillColor: '#f25521'
		}
	}, {
		data: [[1, 5], [3, 7], [5, 10], [7, 7], [9, 9], [11, 5], [13, 4], [15, 6]],
		bars: {
			show: true,
			lineWidth: 0,
			fillColor: '#f9c70a'
		}
	}], {
			grid: {
				borderWidth: 1,
				borderColor: 'transparent'
			},
			yaxis: {
				tickColor: '#transparent',
				font: {
					color: '#000',
					size: 10
				}
			},
			xaxis: {
				tickColor: 'transparent',
				font: {
					color: '#000',
					size: 10
				}
			}
		});

	var newCust = [[0, 2], [1, 3], [2, 6], [3, 5], [4, 7], [5, 8], [6, 10]];
	var retCust = [[0, 1], [1, 2], [2, 5], [3, 3], [4, 5], [5, 6], [6, 9]];

	var plot = $.plot($('#flotLine1'), [
		{
			data: newCust,
			label: 'New Customer',
			color: '#f25521',
			// lines: {
			// 	show: true,
			// 	lineWidth: 2,
			// 	fill: true,
			// 	fillColor: 'rgba(242, 85, 33, 0.3)',
			// 	steps: false
			// },
			points: {
				show: true,
				radius: 3,
				lineWidth: 2,
				fill: true,
				fillColor: '#fff'
			}
		},
		{
			data: retCust,
			label: 'Returning Customer',
			color: '#f9c70a'
		}],
		{
			series: {
				lines: {
					show: true,
					lineWidth: 2
				},
				shadowSize: 4
			},
			points: {
				show: true,
			},
			legend: {
				noColumns: 1,
				position: 'nw', //options : 'ne'
				labelFormatter: function(label, series) {
					return '<span style="color:#000">' + label + '</span>';  // Change the label color to red
				},
			},
			grid: {
				hoverable: true,
				clickable: true,
				borderColor: '#ddd',
				borderWidth: 0,
				labelMargin: 5,
				backgroundColor: { colors: ["#fff", "#eee"] },
				autoHighlight: true,
                mouseActiveRadius: 30
			},
			yaxis: {
				min: 0,
				max: 15,
				ticks: 5,
                tickSize: 3,
                tickFormatter: function(val, axis) {
                        return val + "k"; // Custom format for y-axis ticks
                    },
				color: 'transparent',
				font: {
					size: 10,
					color: '#000'
				}
			},
			xaxis: {
				color: 'transparent',
				font: {
					size: 10,
					color: '#000'
				}
			},
			// tooltip: true,
            //     tooltipOpts: {
            //         content: '%s: %y',
            //         defaultTheme: true,
            //         shifts: {
            //             x: 10,
            //             y: 20
            //         }
            //     },
            //     pan: {
            //         interactive: true,
            //         cursor: "move",
            //         frameRate: 20
            //     },
			// zoom: {
			// 	interactive: true,
			// 	amount: 1.5
			// }
		});

	var plot = $.plot($('#flotLine2'), [
		{
			data: newCust,
			label: 'New Customer',
			color: '#f21780'
		},
		{
			data: retCust,
			label: 'Returning Customer',
			color: '#fd712c'
		}],
		{
			series: {
				lines: {
					show: false
				},
				splines: {
					show: true,
					tension: 0.4,
					lineWidth: 1,
					//fill: 0.4
				},
				shadowSize: 0
			},
			points: {
				show: false,
			},
			legend: {
				noColumns: 1,
				position: 'nw'
			},
			grid: {
				hoverable: true,
				clickable: true,
				borderColor: '#ddd',
				borderWidth: 0,
				labelMargin: 5,
				backgroundColor: 'transparent'
			},
			yaxis: {
				min: 0,
				max: 15,
				color: 'transparent',
				font: {
					size: 10,
					color: '#fff'
				}
			},
			xaxis: {
				color: 'transparent',
				font: {
					size: 10,
					color: '#fff'
				}
			}
		});

	var newCust2 = [[0, 10], [1, 7], [2, 8], [3, 9], [4, 6], [5, 5], [6, 7]];
	var retCust2 = [[0, 8], [1, 5], [2, 6], [3, 8], [4, 4], [5, 3], [6, 6]];

	var plot = $.plot($('#flotLine3'), [
		{
			data: newCust2,
			label: 'New Customer',
			color: '#f21780'
		},
		{
			data: retCust2,
			label: 'Returning Customer',
			color: '#fd712c'
		}],
		{
			series: {
				lines: {
					show: true,
					lineWidth: 1
				},
				shadowSize: 0
			},
			points: {
				show: true,
			},
			legend: {
				noColumns: 1,
				position: 'nw'
			},
			grid: {
				hoverable: true,
				clickable: true,
				borderColor: '#ddd',
				borderWidth: 0,
				labelMargin: 5,
				backgroundColor: 'transparent'
			},
			yaxis: {
				min: 0,
				max: 15,
				color: 'transparent',
				font: {
					size: 10,
					color: '#fff'
				}
			},
			xaxis: {
				color: 'transparent',
				font: {
					size: 10,
					color: '#fff'
				}
			}
		});


	var plot = $.plot($('#flotArea1'), [
		{
			data: newCust,
			label: 'New Customer',
			color: '#4400eb'
		},
		{
			data: retCust,
			label: 'Returning Customer',
			color: '#44ecf5'
		}],
		{
			series: {
				lines: {
					show: true,
					lineWidth: 0,
					fill: 0.8
				},
				shadowSize: 0
			},
			points: {
				show: false,
			},
			legend: {
				noColumns: 1,
				position: 'nw'
			},
			grid: {
				hoverable: true,
				clickable: true,
				borderColor: '#ddd',
				borderWidth: 0,
				labelMargin: 5,
				backgroundColor: 'transparent'
			},
			yaxis: {
				min: 0,
				max: 15,
				color: 'transparent',
				font: {
					size: 10,
					color: '#fff'
				}
			},
			xaxis: {
				color: 'transparent',
				font: {
					size: 10,
					color: '#fff'
				}
			}
		});

	var plot = $.plot($('#flotArea2'), [
		{
			data: newCust,
			label: 'New Customer',
			color: '#36b9d8'
		},
		{
			data: retCust,
			label: 'Returning Customer',
			color: '#4bffa2'
		}],
		{
			series: {
				lines: {
					show: false
				},
				splines: {
					show: true,
					tension: 0.4,
					lineWidth: 0,
					fill: 0.8
				},
				shadowSize: 0
			},
			points: {
				show: false,
			},
			legend: {
				noColumns: 1,
				position: 'nw'
			},
			grid: {
				hoverable: true,
				clickable: true,
				borderColor: '#ddd',
				borderWidth: 0,
				labelMargin: 5,
				backgroundColor: 'transparent'
			},
			yaxis: {
				min: 0,
				max: 15,
				color: 'transparent',
				font: {
					size: 10,
					color: '#fff'
				}
			},
			xaxis: {
				color: 'transparent',
				font: {
					size: 10,
					color: '#fff'
				}
			}
		});

	var previousPoint = null;

	$('#flotLine3, #flotLine4').bind('plothover', function (event, pos, item) {
		$('#x').text(pos.x.toFixed(2));
		$('#y').text(pos.y.toFixed(2));

		if (item) {
			if (previousPoint != item.dataIndex) {
				previousPoint = item.dataIndex;

				$('#tooltip').remove();
				var x = item.datapoint[0].toFixed(2),
					y = item.datapoint[1].toFixed(2);

				showTooltip(item.pageX, item.pageY, item.series.label + ' of ' + x + ' = ' + y);
			}
		} else {

			$('#tooltip').remove();
			previousPoint = null;
		}
	});

	$('#flotLine3, #flotLine4').bind('plotclick', function (event, pos, item) {
		if (item) {
			plot.highlight(item.series, item.datapoint);
		}
	});

	function showTooltip(x, y, contents) {
		$('<div id="tooltip" class="tooltipflot">' + contents + '</div>').css({
			position: 'absolute',
			display: 'none',
			top: y + 5,
			left: x + 5
		}).appendTo('body').fadeIn(200);
	}


	/*********** REAL TIME UPDATES **************/

	var data = [], totalPoints = 50;

	function getRandomData() {
		if (data.length > 0)
			data = data.slice(1);
		while (data.length < totalPoints) {
			var prev = data.length > 0 ? data[data.length - 1] : 50,
				y = prev + Math.random() * 10 - 5;
			if (y < 0) {
				y = 0;
			} else if (y > 100) {
				y = 100;
			}
			data.push(y);
		}
		var res = [];
		for (var i = 0; i < data.length; ++i) {
			res.push([i, data[i]])
		}
		return res;
	}


	// Set up the control widget
	var updateInterval = 1000;

	var plot4 = $.plot('#flotRealtime1', [getRandomData()], {
		colors: ['#f21780'],
		series: {
			lines: {
				show: true,
				lineWidth: 1
			},
			shadowSize: 0	// Drawing is faster without shadows
		},
		grid: {
			borderColor: 'transparent',
			borderWidth: 1,
			labelMargin: 5
		},
		xaxis: {
			color: 'transparent',
			font: {
				size: 10,
				color: '#000'
			}
		},
		yaxis: {
			min: 0,
			max: 100,
			color: 'transparent',
			font: {
				size: 10,
				color: '#000'
			}
		}
	});

	var plot5 = $.plot('#flotRealtime2', [getRandomData()], {
		colors: ['#44ecf5'],
		series: {
			lines: {
				show: true,
				lineWidth: 0,
				fill: 0.9
			},
			shadowSize: 0	// Drawing is faster without shadows
		},
		grid: {
			borderColor: 'transparent',
			borderWidth: 1,
			labelMargin: 5
		},
		xaxis: {
			color: 'transparent',
			font: {
				size: 10,
				color: '#fff'
			}
		},
		yaxis: {
			min: 0,
			max: 100,
			color: 'transparent',
			font: {
				size: 10,
				color: '#fff'
			}
		}
	});

	function update_plot4() {
		plot4.setData([getRandomData()]);
		plot4.draw();
		setTimeout(update_plot4, updateInterval);
	}

	function update_plot5() {
		plot5.setData([getRandomData()]);
		plot5.draw();
		setTimeout(update_plot5, updateInterval);
	}

	update_plot4();
	update_plot5();



})(jQuery);