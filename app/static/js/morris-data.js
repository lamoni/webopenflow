$(function() {

    Morris.Area({
        element: 'morris-area-chart',
        data: [{
            period: '2010 Q1',
            flow1: 2666,
            flow2: null,
            flow3: 2647
        }, {
            period: '2010 Q2',
            flow1: 2778,
            flow2: 2294,
            flow3: 2441
        }, {
            period: '2010 Q3',
            flow1: 4912,
            flow2: 1969,
            flow3: 2501
        }, {
            period: '2010 Q4',
            flow1: 3767,
            flow2: 3597,
            flow3: 5689
        }, {
            period: '2011 Q1',
            flow1: 6810,
            flow2: 1914,
            flow3: 2293
        }, {
            period: '2011 Q2',
            flow1: 5670,
            flow2: 4293,
            flow3: 1881
        }, {
            period: '2011 Q3',
            flow1: 4820,
            flow2: 3795,
            flow3: 1588
        }, {
            period: '2011 Q4',
            flow1: 15073,
            flow2: 5967,
            flow3: 5175
        }, {
            period: '2012 Q1',
            flow1: 10687,
            flow2: 4460,
            flow3: 2028
        }, {
            period: '2012 Q2',
            flow1: 8432,
            flow2: 5713,
            flow3: 1791
        }],
        xkey: 'period',
        ykeys: ['flow1', 'flow2', 'flow3'],
        labels: ['Flow 1', 'Flow 2', 'Flow 3'],
        pointSize: 2,
        hideHover: 'auto',
        resize: true
    });

});