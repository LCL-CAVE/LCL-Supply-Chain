import dash_ag_grid as dag
import pandas as pd
import os


def create_table():
    df = pd.read_csv(os.path.join(
            os.path.dirname('./data/'),
            'solution.csv'))
    return dag.AgGrid(
        rowData=df.to_dict("records"),
        columnDefs=[{"field": i} for i in df.columns],
        className="ag-theme-alpine",
        # columnSize="sizeToFit",
        # className="ag-theme-alpine compact",
        # columnSize="sizeToFit",
    )
