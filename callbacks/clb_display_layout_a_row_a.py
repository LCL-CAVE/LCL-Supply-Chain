from dash import Dash, html, callback, Output, Input
from utils.fig_pie_chart import serve_fig_pie_chart
from app import app


def serve_clb_display_layout_a_row_a(app):
    @app.callback(
        Output("graph_a_a", "figure"),
        Input("btn-drawer-control", "n_clicks"))
    def generate_chart(n_clicks):
        return serve_fig_pie_chart()
