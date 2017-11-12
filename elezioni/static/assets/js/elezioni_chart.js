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
console.log("Ricorda di svuotare la cache quando aggiorni static");
$(function() {
	
	 // Messages area chart
    // ------------------------------
    // Initialize chart
    areaChartWidget("#chart_area_card1", 50, '#5C6BC0');
    areaChartWidget("#chart_area_card2", 50, '#5C6BC0');
    areaChartWidget("#chart_area_card3", 50, '#5C6BC0');
	
	  // Chart setup
    function areaChartWidget(element, chartHeight, color) {


        // Basic setup
        // ------------------------------

        // Define main variables
        var d3Container = d3.select(element),
            margin = {top: 0, right: 0, bottom: 0, left: 0},
            width = d3Container.node().getBoundingClientRect().width - margin.left - margin.right,
            height = chartHeight - margin.top - margin.bottom;

        // Date and time format
        var parseDate = d3.time.format('%Y-%m-%d').parse;


        // Create SVG
        // ------------------------------

        // Container
        var container = d3Container.append('svg');

        // SVG element
        var svg = container
            .attr('width', width + margin.left + margin.right)
            .attr('height', height + margin.top + margin.bottom)
            .append("g")
                .attr("transform", "translate(" + margin.left + "," + margin.top + ")");


        // Construct chart layout
        // ------------------------------

        // Area
        var area = d3.svg.area()
            .x(function(d) { return x(d.date); })
            .y0(height)
            .y1(function(d) { return y(d.value); })
            .interpolate('monotone');


        // Construct scales
        // ------------------------------

        // Horizontal
        var x = d3.time.scale().range([0, width ]);

        // Vertical
        var y = d3.scale.linear().range([height, 0]);


        // Load data
        // ------------------------------
		//var site = "{{url_for('static', filename='assets/demo_data/dashboard/monthly_sales.json')}}";
          //d3.json('/trend_fb_fans1', function (error, data) {
  d3.json('/static/assets/demo_data/dashboard/monthly_sales.json', function (error, data) {

            // Show what's wrong if error
            if (error) return console.error(error);

            // Pull out values
            data.forEach(function (d) {
                d.date = parseDate(d.date);
                d.value = +d.value;
            });
          
            // Get the maximum value in the given array
            var maxY = d3.max(data, function(d) { return d.value; });

            // Reset start data for animation
            var startData = data.map(function(datum) {
                return {
                    date: datum.date,
                    value: 0
                };
            });


            // Set input domains
            // ------------------------------

            // Horizontal
            x.domain(d3.extent(data, function(d, i) { return d.date; }));

            // Vertical
            y.domain([0, d3.max( data, function(d) { return d.value; })]);



            //
            // Append chart elements
            //

            // Add area path
            svg.append("path")
                .datum(data)
                .attr("class", "d3-area")
                .style('fill', color)
                .attr("d", area)
                .transition() // begin animation
                    .duration(1000)
                    .attrTween('d', function() {
                        var interpolator = d3.interpolateArray(startData, data);
                        return function (t) {
                            return area(interpolator (t));
                        };
                    });


            // Resize chart
            // ------------------------------

            // Call function on window resize
            $(window).on('resize', messagesAreaResize);

            // Call function on sidebar width change
            $(document).on('click', '.sidebar-control', messagesAreaResize);

            // Resize function
            // 
            // Since D3 doesn't support SVG resize by default,
            // we need to manually specify parts of the graph that need to 
            // be updated on window resize
            function messagesAreaResize() {

                // Layout variables
                width = d3Container.node().getBoundingClientRect().width - margin.left - margin.right;


                // Layout
                // -------------------------

                // Main svg width
                container.attr("width", width + margin.left + margin.right);

                // Width of appended group
                svg.attr("width", width + margin.left + margin.right);

                // Horizontal range
                x.range([0, width]);


                // Chart elements
                // -------------------------

                // Area path
                svg.selectAll('.d3-area').datum( data ).attr("d", area);
            }
        });
    }
});
