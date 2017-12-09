/* ------------------------------------------------------------------------------
*
*  # Vector maps
*
*  Specific JS code additions for maps_vector.html page
*
*  Version: 1.0
*  Latest update: Aug 1, 2015
*
* ---------------------------------------------------------------------------- */

$(function() {
  
  function getRegionCentroid(region, map) {
      bbox = region.element.node.getBBox();
      xcoord = (((bbox.x + bbox.width/2)+map.transX)*map.scale);
      ycoord = (((bbox.y + bbox.height/2)+map.transY)*map.scale);
      pp = map.pointToLatLng(xcoord,ycoord);
      return [pp.lat,pp.lng];
  };
  
  function addMarkers(data, map){
      markers = [];
      markersValues = [];
      provincie = map.regions;
      for (var i = 0; i < data.length; i++){
      for (p in provincie){
      if(data[i].codice == p){
      point = getRegionCentroid(map.regions[p],map);
      centroid = {
      "latLng" : point,
      "name" : data[i].provincia
      };
      markers.push(centroid);
      markersValues.push(data[i].menzioni);
      };
      };
  
      };
  
      map.addMarkers(markers, []);
      map.series.markers[0].setValues(markersValues);
      //console.log(map.labels);
  };
  
  $.getJSON('/mappa_pd', function(data){
    // World map PD
    menzioni = [];
    for (var i = 0; i < data.length; i++){
            menzioni.push(data[i].menzioni);
    };
    var min = Math.min.apply(null, menzioni);
    var max = Math.max.apply(null, menzioni);
    $('.map-world-1').vectorMap({
        map: 'it_mill',
        backgroundColor: 'transparent',
        regionStyle: {
            initial: {
                fill: '#93D389'
            }
        },
        markerStyle: {
            initial: {
                fill: 'red',
                stroke: '#383f47'
            }
        },
        markers: [],
        series: {
            markers: [{
                attribute: 'r',
                scale: [5, 20],
                values: [],
                min: min,
                max: max
            }]
        }
    });
            
            
    // Aggiungo i Markers Dinamicamente
    var map=$('.map-world-1').vectorMap('get','mapObject');
    addMarkers(data,map);
  });
  
  $.getJSON('/mappa_m5s', function(data){
          // World map M5S
            menzioni = [];
            for (var i = 0; i < data.length; i++){
            menzioni.push(data[i].menzioni);
            };
            var min = Math.min.apply(null, menzioni);
            var max = Math.max.apply(null, menzioni);
          $('.map-world-2').vectorMap({
                map: 'it_mill',
                backgroundColor: 'transparent',
                regionStyle: {
                    initial: {
                        fill: '#93D389'
                            }
                    },
                    markerStyle: {
                            initial: {
                            fill: '#F8E23B',
                            stroke: '#383f47'
                            }
                    },
                markers: [],
                series: {
                    markers: [{
                        attribute: 'r',
                        scale: [5, 20],
                        values: [],
                        min: min,
                        max: max
                    }]
                }
           });
            
          // Aggiungo i Markers Dinamicamente
            var map=$('.map-world-2').vectorMap('get','mapObject');
            addMarkers(data,map);
        });
  
  $.getJSON('/mappa_silvio', function(data){
            menzioni = [];
            for (var i = 0; i < data.length; i++){
            menzioni.push(data[i].menzioni);
            };
            var min = Math.min.apply(null, menzioni);
            var max = Math.max.apply(null, menzioni);
  // World map silvio
  $('.map-world-3').vectorMap({
        map: 'it_mill',
        backgroundColor: 'transparent',
        regionStyle: {
        initial: {
            fill: '#93D389'
        }
        },
        markerStyle: {
            initial: {
                fill: 'black',
                stroke: '#383f47'
            }
        },
        markers: [],
        series: {
                markers: [{
                    attribute: 'r',
                    scale: [5, 20],
                    values: [],
                    min: min,
                    max: max
                }]
        }
    });
            // Aggiungo i Markers Dinamicamente
            var map=$('.map-world-3').vectorMap('get','mapObject');
            addMarkers(data,map);
    });
  
});
