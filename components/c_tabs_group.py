from layouts.ly_display_result_a_layout import create_display_result_a_layout
from components.c_table import create_table
import dash_mantine_components as dmc


def create_tabs_group():
    return dmc.Tabs(
        [
            dmc.TabsList(
                [
                    dmc.Tab("Overview", value="1"),
                    dmc.Tab("Detailed results", value="2"),
                ]

            ),
            dmc.TabsPanel(
                create_display_result_a_layout(),
                value="1"),
            dmc.TabsPanel(
                create_table(),
                value="2"
            ),
        ],
        value="1",
    )
