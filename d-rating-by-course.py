import justpy as jp
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from pytz import utc
data=pd.read_csv('reviews.csv',parse_dates=['Timestamp'])
nrs = data.groupby(['Course Name'])['Rating'].count()

chart_def = """

 {
    chart: {
        plotBackgroundColor: null,
        plotBorderWidth: null,
        plotShadow: false,
        type: 'pie'
    },
    title: {
        text: 'Browser market shares in January, 2018'
    },
    tooltip: {
        pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
    },
    accessibility: {
        point: {
            valueSuffix: '%'
        }
    },
    plotOptions: {
        pie: {
            allowPointSelect: true,
            cursor: 'pointer',
            dataLabels: {
                enabled: true,
                format: '<b>{point.name}</b>: {point.percentage:.1f} %'
            }
        }
    },
    series: [{
        name: 'Rating',
        colorByPoint: true,
        data: [{
            name: 'Chrome',
            y: 61.41,
            sliced: true,
            selected: true
        }, {
            name: 'Internet Explorer',
            y: 11.84
        }, {
            name: 'Firefox',
            y: 10.85
        }, {
            name: 'Edge',
            y: 4.67
        }, {
            name: 'Safari',
            y: 4.18
        }, {
            name: 'Sogou Explorer',
            y: 1.64
        }, {
            name: 'Opera',
            y: 1.6
        }, {
            name: 'QQ',
            y: 1.2
        }, {
            name: 'Other',
            y: 2.61
        }]
    }]
}

"""

def app():
    # Creating a web page
    wp = jp.QuasarPage() 

    # heading
    h1 = jp.QDiv(a=wp, text='Analysis of Course Reviews',classes="text-h3 text-center text-weight-bold")
    
    # Displaying the chart
    hc = jp.HighCharts(a=wp,options=chart_def)

    #title of the chart
    hc.options.title.text = "Number of Rating by Course"
    hc.options.subtitle.text = "According the provided dataset"

    #taking the dataset from the given dataframe
    hc_data = [{"name":v1,"y":v2}for v1,v2 in zip(nrs.index,nrs)]
    hc.options.series[0].data = hc_data


    return wp

jp.justpy(app)
