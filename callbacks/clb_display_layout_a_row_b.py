from dash import Dash, html, callback, Output, Input
from utils.fig_bar_chart import serve_fig_bar_chart
from app import app


def serve_clb_display_layout_a_row_b(app):
    @app.callback(
        Output("graph_a_b", "figure"),
        Input("btn-drawer-control", "n_clicks"))
    def generate_chart(n_clicks):
        return serve_fig_bar_chart()
