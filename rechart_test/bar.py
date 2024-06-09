import reflex as rx
import random

init_data = [
    {"name": "Page A", "uv": 4000, "pv": 2400, "amt": 2400},
    {"name": "Page B", "uv": 3000, "pv": 1398, "amt": 2210},
    {"name": "Page C", "uv": 2000, "pv": 9800, "amt": 2290},
    {"name": "Page D", "uv": 2780, "pv": 3908, "amt": 2000},
    {"name": "Page E", "uv": 1890, "pv": 4800, "amt": 2181},
    {"name": "Page F", "uv": 2390, "pv": 3800, "amt": 2500},
    {"name": "Page G", "uv": 3490, "pv": 4300, "amt": 2100},
]


def bar_1():
    return rx.recharts.bar_chart(
        rx.recharts.bar(
            data_key="uv", 
            stroke=rx.Var.create_safe(rx.color("accent", 8), _var_is_string=True),
            fill=rx.Var.create_safe(rx.color("accent", 3), _var_is_string=True),
        ),
        rx.recharts.x_axis(data_key="name"),
        rx.recharts.y_axis(),
        data=init_data,
        height = 200,
        width = 500
    )

data = [
    {'name': 'Page A', 'value': 2400},
    {'name': 'Page B', 'value': 1398},
    {'name': 'Page C', 'value': 9800},
    {'name': 'Page D', 'value': 3908},
    {'name': 'Page E', 'value': 4800},
    {'name': 'Page F', 'value': 3800},
]

def bar_2():
    return rx.recharts.bar_chart(
        rx.recharts.bar(
            data_key="value",
            fill="#8884d8",
        ),
        rx.recharts.x_axis(data_key="name"),
        rx.recharts.y_axis(data_key="value"),
        data=data,
        layout="vertical",
        width=500,
        height=300,
    )

def bar_3():
    return rx.recharts.bar_chart(
        rx.recharts.bar(
            data_key="value",
            fill="#8884d8",
        ),
        rx.recharts.x_axis(data_key="name"),
        rx.recharts.y_axis(),
        data=data,
        bar_category_gap="15%",
        bar_gap=6,
        bar_size=24,
        max_bar_size=40,
        width=500,
        height=300,
    )

class BarState(rx.State):
    data = init_data

    def randomize_data(self):
        for i in range(len(self.data)):
            self.data[i]["uv"] = random.randint(0, 10000)
            self.data[i]["pv"] = random.randint(0, 10000)
            self.data[i]["amt"] = random.randint(0, 10000)

def bar_4():
    return rx.recharts.bar_chart(
        rx.recharts.bar(
            data_key="uv", 
            stroke="#8884d8", 
            fill="#8884d8", 
        ),
        rx.recharts.bar(
            data_key="pv",
            stroke="#82ca9d", 
            fill="#82ca9d", 
        ),
        rx.recharts.x_axis(data_key="name"),
        rx.recharts.y_axis(),
        rx.recharts.legend(),
        rx.recharts.cartesian_grid(
            stroke_dasharray="3 3",
        ),
        on_click=BarState.randomize_data,
        data=BarState.data,
        width = 600,
        height = 300,
    )

def show():
    return rx.vstack(
        bar_1(),
        bar_2(),
        bar_3(),
    )