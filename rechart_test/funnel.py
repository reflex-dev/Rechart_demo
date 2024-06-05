import reflex as rx
import random

data = [
    {"value": 100, "name": "Sent", "fill": "#8884d8"},
    {"value": 80, "name": "Viewed", "fill": "#83a6ed"},
    {"value": 50, "name": "Clicked", "fill": "#8dd1e1"},
    {"value": 40, "name": "Add to Cart", "fill": "#82ca9d"},
    {"value": 26, "name": "Purchased", "fill": "#a4de6c"},
]

class FunnelState(rx.State):
    data = data

    def randomize_data(self):
        self.data[0]["value"] = 100
        for i in range(len(self.data) - 1):
            self.data[i + 1]["value"] = self.data[i][
                "value"
            ] - random.randint(0, 20)


def show():
    return rx.recharts.funnel_chart(
        rx.recharts.funnel(
            rx.recharts.label_list(
                position="right",
                data_key="name",
                fill="#000",
                stroke="none",
            ),
            data_key="value",
            data=FunnelState.data,
            # on_click=FunnelState.randomize_data,
            # on_click is missing
        ),
        rx.recharts.graphing_tooltip(),
        width=500,
        height=250,
    )