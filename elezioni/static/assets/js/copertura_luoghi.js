/* ------------------------------------------------------------------------------
*
*  # Statistics widgets
*
*  Specific JS code additions for general_widgets_stats.html page
*
*  Version: 1.0
*  Latest update: Mar 20, 2017
*
* ---------------------------------------------------------------------------- */
$(function() {
	
  // Segmented gauge
  // ------------------------------
  
  var luoghi1 = document.getElementById('luoghi1').getAttribute('data-luoghi1');
  var luoghi2 = document.getElementById('luoghi2').getAttribute('data-luoghi2');
  var luoghi3 = document.getElementById('luoghi3').getAttribute('data-luoghi3');
  
  // Initialize chart
  segmentedGauge("#segmented_gauge", 200, 0, 100, 5, luoghi1);
  segmentedGauge("#segmented_gauge_2", 200, 0, 100, 5, luoghi2);
  segmentedGauge("#segmented_gauge_3", 200, 0, 100, 5, luoghi3);
  
  // Setup chart
  function segmentedGauge(element, size, min, max, sliceQty, value) {
  
  // Main variables
  var d3Container = d3.select(element),
  width = size,
  height = (size / 2) + 20,
  radius = (size / 2),
  ringInset = 15,
  ringWidth = 20,
  
  pointerWidth = 10,
  pointerTailLength = 5,
  pointerHeadLengthPercent = 0.75,
  
  minValue = min,
  maxValue = max,
  
  minAngle = -90,
  maxAngle = 90,
  
  slices = sliceQty,
  range = maxAngle - minAngle,
  pointerHeadLength = Math.round(radius * pointerHeadLengthPercent);
  
  // Colors
  var colors = d3.scale.linear()
  .domain([0, slices - 1])
  .interpolate(d3.interpolateHsl)
  .range(['#66BB6A', '#EF5350']);
  
  
  // Create chart
  // ------------------------------
  
  // Add SVG element
  var container = d3Container.append('svg');
  
  // Add SVG group
  var svg = container
  .attr('width', width)
  .attr('height', height);
  
  
  // Construct chart layout
  // ------------------------------
  
  // Donut
  var arc = d3.svg.arc()
  .innerRadius(radius - ringWidth - ringInset)
  .outerRadius(radius - ringInset)
  .startAngle(function(d, i) {
              var ratio = d * i;
              return deg2rad(minAngle + (ratio * range));
              })
  .endAngle(function(d, i) {
            var ratio = d * (i + 1);
            return deg2rad(minAngle + (ratio * range));
            });
  
  // Linear scale that maps domain values to a percent from 0..1
  var scale = d3.scale.linear()
  .range([0, 1])
  .domain([minValue, maxValue]);
  
  // Ticks
  var ticks = scale.ticks(slices);
  var tickData = d3.range(slices)
  .map(function() {
       return 1 / slices;
       });
  
  // Calculate angles
  function deg2rad(deg) {
  return deg * Math.PI / 180;
  }
  
  // Calculate rotation angle
  function newAngle(d) {
  var ratio = scale(d);
  var newAngle = minAngle + (ratio * range);
  return newAngle;
  }
  
  
  // Append chart elements
  // ------------------------------
  
  //
  // Append arc
  //
  
  // Wrap paths in separate group
  var arcs = svg.append('g')
  .attr('transform', "translate(" + radius + "," + radius + ")")
  .style({
         'stroke': '#fff',
         'stroke-width': 2,
         'shape-rendering': 'crispEdges'
         });
  
  // Add paths
  arcs.selectAll('path')
  .data(tickData)
  .enter()
  .append('path')
  .attr('fill', function(d, i) {
        return colors(i);
        })
  .attr('d', arc);
  
  
  //
  // Text labels
  //
  
  // Wrap text in separate group
  var arcLabels = svg.append('g')
  .attr('transform', "translate(" + radius + "," + radius + ")");
  
  // Add text
  arcLabels.selectAll('text')
  .data(ticks)
  .enter()
  .append('text')
  .attr('transform', function(d) {
        var ratio = scale(d);
        var newAngle = minAngle + (ratio * range);
        return 'rotate(' + newAngle + ') translate(0,' + (10 - radius) + ')';
        })
  .style({
         'text-anchor': 'middle',
         'font-size': 11,
         'fill': '#999'
         })
  .text(function(d) { return d + "%"; });
  
  
  //
  // Pointer
  //
  
  // Line data
  var lineData = [
                  [pointerWidth / 2, 0],
                  [0, -pointerHeadLength],
                  [-(pointerWidth / 2), 0],
                  [0, pointerTailLength],
                  [pointerWidth / 2, 0]
                  ];
  
  // Create line
  var pointerLine = d3.svg.line()
  .interpolate('monotone');
  
  // Wrap all lines in separate group
  var pointerGroup = svg
  .append('g')
  .data([lineData])
  .attr('transform', "translate(" + radius + "," + radius + ")");
  
  // Paths
  pointer = pointerGroup
  .append('path')
  .attr('d', pointerLine)
  .attr('transform', 'rotate(' + minAngle + ')');
  
  var ratio = scale(value * max);
  var newAngle = minAngle + (ratio * range);
  pointer.transition()
  .duration(2500)
  .ease('elastic')
  .attr('transform', 'rotate(' + newAngle + ')');
  
  }
  
});
