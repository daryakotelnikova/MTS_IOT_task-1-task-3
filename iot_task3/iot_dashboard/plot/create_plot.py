import json

import plotly
import plotly.graph_objs as go


def create_plot(df, column):
    data = [
        go.Scatter(
            x=df["ts"],
            y=df[column]
        )
    ]

    return json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)
