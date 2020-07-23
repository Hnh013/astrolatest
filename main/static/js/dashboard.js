$(function () {
    "use strict";

    // LINE CHART
	Morris.Area({
        element: 'line-chart',
        data: [{
            period: '2019-05-10',
            view: 50,
            share: 80,
            bookmark: 20
        }, {
            period: '2019-05-11',
            view: 130,
            share: 100,
            bookmark: 80
        }, {
            period: '2019-05-12',
            view: 80,
            share: 60,
            bookmark: 70
        }, {
            period: '2019-05-13',
            view: 70,
            share: 200,
            bookmark: 140
        }, {
            period: '2019-05-14',
            view: 180,
            share: 150,
            bookmark: 140
        }, {
            period: '2019-05-15',
            view: 105,
            share: 100,
            bookmark: 80
        },
         {
            period: '2019-05-16',
            view: 250,
            share: 150,
            bookmark: 200
        }],
        xkey: 'period',
        ykeys: ['view', 'share', 'bookmark'],
        labels: ['View', 'Share', 'Book mark'],
        pointSize: 3,
		xLabels: 'day',
        fillOpacity: 0,
        pointStrokeColors:['#1cc100', '#fdc006', '#1db4bd'],
        behaveLikeLine: true,
        gridLineColor: '#e0e0e0',
        lineWidth: 1,
        hideHover: 'auto',
        lineColors: ['#1cc100', '#fdc006', '#1db4bd'],
        resize: true
        
    });

}); 