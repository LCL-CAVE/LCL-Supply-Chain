import dash_leaflet as dl
import os
import pandas as pd

df = pd.read_csv(os.path.join(
    os.path.dirname('./data/'),
    'nodes.csv'), delimiter=';', decimal=",")


def create_map_marker():
    return [
        dl.Marker(position=[
            df['latitude'].iloc[i],
            df['longitude'].iloc[i]],
            icon=dict(
                iconUrl='/assets/' + str(df['type'].iloc[i]) + '.svg',
                iconSize=[30, 80],
            ),
            children=[
                dl.Tooltip(
                    content=str(df['node'].iloc[i]) + '<br>' + str(
                        df['param_name'].iloc[i]) + ": " + str(
                        df['param_value'].iloc[i]),className="marker-map")
            ]
        )
        for i in range(df.shape[0])
    ]
