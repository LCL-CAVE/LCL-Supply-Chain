import dash_ag_grid as dag
from dash import html, dcc
from utils.utils import create_graph
import dash_mantine_components as dmc


def create_graph_group():
    return [
        html.Div(dcc.Graph(id="graph_a_a", config={'displayModeBar': False}, ),
                 className="drawer-fig-layout"),
        html.Div(dcc.Graph(id="graph_a_b", config={'displayModeBar': False}, ),
                 className="drawer-fig-layout"),
        html.Div(dcc.Graph(id="graph_a_c", config={'displayModeBar': False}, ),
                 className="drawer-fig-layout"),
    ]
