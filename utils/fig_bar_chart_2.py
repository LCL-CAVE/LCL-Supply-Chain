import plotly.express as px
import pandas as pd
import os

def serve_fig_bar_chart_2():
    df = pd.read_csv(os.path.join(
        os.path.dirname('./data/'),
        'warehouse_util.csv'), delimiter=';', decimal=",")
    fig = px.bar(df, x='node', y='param_value',
                 # hover_data=['lifeExp', 'gdpPercap'], color='lifeExp',
                 # labels={'pop': 'population of Canada'},
                 height=400)
    # Update layout
    fig.update_layout(
        font=dict(
            family="Courier New, monospace",
            size=16,
        ),
        title=dict(
            text="Warehouse utilization",
            font=dict(size=16),
            automargin=True,
            yref='container',
            x=0.05,
            y=0.95,
        ),
        margin=dict(
            l=40,
            r=40,
            b=40,
            t=40
        ),
        yaxis={
            'title': None,
            'linecolor': "#D3D3D3",
            # 'ticklabelposition': 'inside',
            'showgrid': False
        },
        xaxis={
            'title': None,
            'linecolor': "#D3D3D3",
            # 'ticklabelposition': 'inside',
            'showgrid': False
        },
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        legend=dict(yanchor="top", y=0.99, xanchor="right", x=0.99),
        hoverlabel=dict(
            bgcolor='rgba(0,0,0,.9)',
            font_size=16,
            font_family="Rockwell"
        ),
    )
    return fig
