import plotly.express as px


def serve_fig_pie_chart():
    df = px.data.tips()  # replace with your own data source
    fig = px.pie(df, values="total_bill", names="day", hole=.3)
    # Update layout
    fig.update_layout(
        font=dict(
            family="Courier New, monospace",
            size=18,
            color="RebeccaPurple"
        ),
        title=dict(
            text="Cost Reduction",
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
