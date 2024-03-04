from layouts.ly_control_layout import create_control_layout
from layouts.ly_header_layout import create_header_layout
from layouts.ly_map_layout import create_map_layout
from components.c_display_notification_progress import create_notification_progress
from layouts.ly_drawer_layout import create_drawer_layout
import dash_mantine_components as dmc
from dash import Dash, html, callback, Output, Input

app = Dash(
    __name__,
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1.0"}
    ],
    external_stylesheets=[
        "https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,100;0,300;0,400;0,500;0,700;0,900;1,100;1,300;1,"
        "400;1,500;1,700;1,900&display=swap",
    ],
)

app.title = "LCL-Supply-Chain"
server = app.server
app.scripts.config.serve_locally = True
app.css.config.serve_locally = True
app.config.suppress_callback_exceptions = True

app.layout = dmc.MantineProvider(
    id="theme-app",
    children=[
        dmc.LoadingOverlay(
            dmc.Paper(
                [
                    create_header_layout(),
                    create_map_layout(),
                    create_control_layout(),
                    create_drawer_layout(),
                ],
            ),
            id="loading-layout"
        ),
        create_notification_progress(),
    ],
    withGlobalStyles=True,
    inherit=True,
    withNormalizeCSS=True,
    theme={
        "colorScheme": "light",
    },

)

if __name__ == "__main__":
    from callbacks import clb_display_notif_progress, clb_display_loading, clb_update_arcs, clb_display_drawer, \
        clb_display_layout_a_row_a, clb_display_layout_a_row_b, clb_display_layout_a_row_c

    clb_display_notif_progress.serve_clb_display_notif_stage_a(app)
    clb_display_notif_progress.serve_clb_display_notif_stage_b(app)
    clb_display_loading.serve_clb_display_loading(app)
    clb_update_arcs.serve_clb_update_arcs(app)
    clb_display_drawer.serve_clb_display_drawer(app)
    clb_display_layout_a_row_a.serve_clb_display_layout_a_row_a(app)
    clb_display_layout_a_row_b.serve_clb_display_layout_a_row_b(app)
    clb_display_layout_a_row_c.serve_clb_display_layout_a_row_c(app)

    app.run_server(debug=True)
