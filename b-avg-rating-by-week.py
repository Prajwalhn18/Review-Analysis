from ssl import Options
from typing import Text
import justpy as jp
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from pytz import utc
data=pd.read_csv('reviews.csv',parse_dates=['Timestamp'])

#calculation of the average rating per week
data['Week'] = data['Timestamp'].dt.strftime('%Y-%U')
week_average = data.groupby(['Week']).mean()

from pandas.core.dtypes.common import classes

#template of code from HighChart for better presentation of graph
chart_def="""
{
    chart: {
        type: 'spline',
        inverted: false
    },
    title: {
        text: 'Atmosphere Temperature by Altitude'
    },
    subtitle: {
        text: 'According to the Standard Atmosphere Model'
    },
    xAxis: {
        reversed: false,
        title: {
            enabled: true,
            text: 'Week'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: 'Range: 0 to 80 km.'
        },
        maxPadding: 0.05,
        showLastLabel: true
    },
    yAxis: {
        title: {
            text: 'Average Rating'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: 'Range: -90°C to 20°C.'
        },
        lineWidth: 2
    },
    legend: {
        enabled: false
    },
    tooltip: {
        headerFormat: '<b>{series.name}</b><br/>',
        pointFormat: '{point.x}: {point.y}'
    },
    plotOptions: {
        spline: {
            marker: {
                enable: false
            }
        }
    },
    series: [{
        name: 'Average Rating',
        data: [[0, 15], [10, -50], [20, -56.5], [30, -46.5], [40, -22.1],
            [50, -2.5], [60, -27.7], [70, -55.7], [80, -76.5]]
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
    hc.options.title.text = "Average Rating by Week"
    hc.options.subtitle.text = "According the provided dataset"

    #taking the dataset from the given dataframe
    hc.options.xAxis.categories = list(week_average.index)
    hc.options.series[0].data = list(week_average['Rating'])


    return wp

jp.justpy(app)


