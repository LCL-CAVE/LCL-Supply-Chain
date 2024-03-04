from dash import Dash, html, callback, Output, Input
from utils.fig_bar_chart_2 import serve_fig_bar_chart_2
from app import app


def serve_clb_display_layout_a_row_c(app):
    @app.callback(
        Output("graph_a_c", "figure"),
        Input("btn-drawer-control", "n_clicks"))
    def generate_chart(n_clicks):
        return serve_fig_bar_chart_2()