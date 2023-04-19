var chart = Highcharts.chart('container', {
    chart: {
        type: 'column',
        width: 300,
        height: 300,
        margin: [50, 0, 50, 100]
    },
    title: {
        text: '',
        margin: 0
    },
    tooltip: {
        enabled: false
    },
    yAxis: {
        min: 0,
        tickInterval: 20,
        max: 100,
        title: {
            text: y_title,
            margin: 16,
            style: {
                fontSize: 13
            }
        },
        labels: {
            format: '{value} ECU',
            style: {
                fontSize: 13
            }
        }
    },
    xAxis: {
        type: 'category',
        tickLength: 0,
        labels: {
            style: {
                fontSize: 13
            }
        }
    },
    plotOptions: {
        column: {
            pointPadding: 0.2,
            pointWidth: 50,
            borderWidth: 0,
            columnWidth: 20
        }
    },
    series: [{
        data: [{
            name: "A",
            y: asset_a,
            color: 'rgba(0,123,255,0.5)'
        },{
            name: "B",
            y: asset_b,
            color: 'rgba(40,167,69,0.5)'
        }],
        showInLegend: false
    }],
    credits: {
        enabled: false
    },
    exporting: {
        enabled: false
    }
});


$('input[id=asset_a]').keyup(function () {
    chart.series[0].data[0].update([parseFloat($(this).val())]);
});

$('input[id=asset_b]').keyup(function () {
    chart.series[0].data[1].update([parseFloat($(this).val())]);
});