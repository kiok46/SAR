window.onload = $(function () {
    $('#container').highcharts({
        chart: {
            type: 'column'
        },
        title: {
            text: 'Sentiment Analysis'
        },
        xAxis: {
            categories: ['Reaction']
        },
        credits: {
            enabled: false
        },
        series: [{
            name: 'Positive',
            data: [0.56]
        }, {
            name: 'Negative',
            data: [-0.45]
        },
        ]
    });
});
