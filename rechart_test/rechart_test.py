"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config

from . import area
from . import axis
from . import bar
from . import brush
from . import cartesian_grid
from . import composed_chart
from . import error_bar
from . import funnel
from . import label
from . import legend
from . import line
from . import pie
from . import radar
from . import reference
from . import ScatterChart
from . import tooltip
from . import tree



class State(rx.State):
    """The app state."""
    display: str = "Axis"

    def set_display(self, selection):
        self.display = selection


def charts():
    return rx.vstack(
        rx.select(
            ["Area", "Axis", "Bar", "Brush", "CartesianGrid", "ErrorBar", "Funnel", "Label", "Legend", "Line", "Pie", "Tree", "Radar", "ComposedChart", "Reference", "Tooltip", "ScatterChart"],
            variant="soft",
            radius="full",
            width="60%",
            default_value="Axis",
            on_change=State.set_display,
        ),
        rx.match(
            State.display,
            ("Area", area.show()),
            ("Axis", axis.show()),
            ("Bar", bar.show()),
            ("Brush", brush.show()),
            ("CartesianGrid", cartesian_grid.show()),
            ("ErrorBar", error_bar.show()),
            ("Funnel", funnel.show()),
            ("Label", label.show()),
            ("Legend", legend.show()),
            ("Line", line.show()),
            ("Pie", pie.show()),
            ("Radar", radar.show()),
            ("Reference", reference.show()),
            ("ComposedChart", composed_chart.show()),
            ("Tooltip", tooltip.show()),
            ("ScatterChart", ScatterChart.show()),
            ("Tree", tree.show()),
            tree.show(),
        ),
        width = "100%",
        height = "100%",
        spacing = "8"
    )


def index() -> rx.Component:
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Recharts Playground", size="8"),
            charts(),
            spacing="5",
            justify="center",
            min_height="100vh",
        ),
        rx.logo(),
    )


app = rx.App()
app.add_page(index)
