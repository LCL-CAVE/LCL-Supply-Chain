from app import app
import dash_leaflet as dl
from dash import Input, Output
import time
import os
import numpy as np
import pandas as pd


def serve_clb_update_arcs(app):
    @app.callback(Output('position-data', 'children'),
                  Input("btn_run", "n_clicks"),
                  prevent_initial_call=True)
    def update_arcs(n_clicks):
        time.sleep(5)
        df = pd.read_csv(os.path.join(
            os.path.dirname('./data/'),
            'nodes.csv'), delimiter=';', decimal=",")
        df2 = pd.DataFrame(columns=['origin', 'destination', 'transport_value'])
        arcs = {}
        for p in range(20):
            i = np.random.randint(0, 8)
            j = np.random.randint(8, 16)
            k = np.random.randint(16, 28)
            df2.at[p, 'origin'] = df['node'].iloc[i] + " - " + df['country'].iloc[i]
            df2.at[p, 'destination'] = df['node'].iloc[j] + " - " + df['country'].iloc[j]
            df2.at[p, 'transport_value'] = np.random.randint(500, 999)
            arcs.update({f"'{p}'": [[df['latitude'].iloc[i], df['longitude'].iloc[i]],
                                    [df['latitude'].iloc[j], df['longitude'].iloc[j]]]})
            arcs.update({f"'{p + 50}'": [[df['latitude'].iloc[j], df['longitude'].iloc[j]],
                                         [df['latitude'].iloc[k], df['longitude'].iloc[k]]]})
        arcs_polyline = []
        df2.to_csv("./data/solution.csv", index=False)
        for p in arcs.values():
            arcs_polyline += [
                dl.Polyline(positions=p, children=[dl.Tooltip(content=str(np.random.randint(500, 999)))], color='red')
            ]
        return arcs_polyline
