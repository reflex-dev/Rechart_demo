import reflex as rx
import random

data = [
    {"name": "Page A", "uv": 4000, "pv": 2400, "amt": 2400},
    {"name": "Page B", "uv": 3000, "pv": 1398, "amt": 2210},
    {"name": "Page C", "uv": 2000, "pv": 3800, "amt": 2290},
    {"name": "Page D", "uv": 2780, "pv": 3908, "amt": 2000},
    {"name": "Page E", "uv": 1890, "pv": 4800, "amt": 2181},
    {"name": "Page F", "uv": 2390, "pv": 3800, "amt": 2500},
    {"name": "Page G", "uv": 3490, "pv": 4300, "amt": 2100},
]

data2 = [
    {"day": "05-01", "temperature": [-1, 10]},
    {"day": "05-02", "temperature": [2, 15]},
    {"day": "05-03", "temperature": [3, 12]},
    {"day": "05-04", "temperature": [4, 12]},
    {"day": "05-05", "temperature": [12, 17]},
    {"day": "05-06", "temperature": [5, 16]},
    {"day": "05-07", "temperature": [3, 12]},
    {"day": "05-08", "temperature": [0, 8]},
    {"day": "05-09", "temperature": [-3, 5]},
]

def area_1():
    """
    usage: weight, height, area.stroke, area.fill, area.type_, GraphingToolTip"""
    return rx.recharts.area_chart(
        rx.recharts.area(
            data_key="uv",
            stroke=rx.Var.create_safe(rx.color("accent", 8), _var_is_string=True),
            fill=rx.Var.create_safe(rx.color("accent", 3), _var_is_string=True),
            type_ = "monotone",
        ),
        rx.recharts.x_axis(data_key="name"),
        rx.recharts.y_axis(),
        rx.recharts.GraphingTooltip(),
        data=data,
        height = 300,
        width = 500,
    )

def area_2():
    return rx.recharts.area_chart(
        rx.recharts.area(
            data_key="uv", stroke="#8884d8", fill="#8884d8", stack_id="1", 
        ),
        rx.recharts.area(
            data_key="pv", stroke="#82ca9d", fill="#82ca9d", stack_id="1",
        ),
        rx.recharts.x_axis(data_key="name"),
        rx.recharts.y_axis(),
        data=data,
        stack_offset="none",
        margin={"top": 5, "right": 5, "bottom": 5, "left": 5},
        height = 300,
        width = 500,
    )

def area_3():
    return rx.recharts.area_chart(
        rx.recharts.area(
            data_key="temperature",
            stroke="#8884d8",
            fill="#8884d8"
        ), 
        rx.recharts.x_axis(data_key="day"), 
        rx.recharts.y_axis(),
        data=data2,
        height = 300,
        width = 500,
    )

class AreaState(rx.State):
    data = data
    curve_type = ""
    def randomize_data(self):
        for i in range(len(self.data)):
            self.data[i]["uv"] = random.randint(0, 10000)
            self.data[i]["pv"] = random.randint(0, 10000)
            self.data[i]["amt"] = random.randint(0, 10000)

    def change_curve_type(self, type_input):
        self.curve_type = type_input

def area_4():
    return rx.vstack(
        rx.select(
            [
                'basis',
                'basisClosed',
                'basisOpen',
                'bumpX',
                'bumpY',
                'bump',
                'linear',
                'linearClosed',
                'natural',
                'monotoneX',
                'monotoneY',
                'monotone',
                'step',
                'stepBefore',
                'stepAfter'
            ],
            on_change = AreaState.change_curve_type,
            default = 'basis',
        ),
        rx.recharts.area_chart(
            rx.recharts.area(
                data_key="uv",
                stroke="#8884d8",
                fill="#8884d8",
                on_click=AreaState.randomize_data,
                type_ = AreaState.curve_type,
            ),
            rx.recharts.area(
                data_key="pv",
                stroke="#82ca9d",
                fill="#82ca9d",
                on_click=AreaState.randomize_data,
                type_ = AreaState.curve_type,
            ),
            rx.recharts.x_axis(
                data_key="name",
            ),
            rx.recharts.y_axis(),
            rx.recharts.legend(),
            rx.recharts.cartesian_grid(
                stroke_dasharray="3 3",
            ),
            data=AreaState.data,
            width=500,
            height=400,
        )
    )

def area_5():
    return rx.vstack(
        rx.recharts.bar_chart(
            rx.recharts.bar(
                data_key="uv", stroke="#8884d8", fill="#8884d8"
            ),
            rx.recharts.bar(
                data_key="pv", stroke="#82ca9d", fill="#82ca9d",
            ),
            rx.recharts.x_axis(data_key="name"),
            rx.recharts.y_axis(),
            rx.recharts.graphing_tooltip(),
            data=data,
            sync_id="1",
            width = 600,
            height = 250,
        ),
        rx.recharts.composed_chart(
            rx.recharts.area(
                data_key="uv", stroke="#8884d8", fill="#8884d8"
            ),
            rx.recharts.bar(
                data_key="amt", fill="#413ea0"
            ),
            rx.recharts.bar(
                data_key="pv", stroke="#82ca9d", fill="#82ca9d",
            ),
            rx.recharts.line(
                data_key="pv", type_="monotone", stroke="#ff7300",
            ),
            
            rx.recharts.x_axis(data_key="name"),
            rx.recharts.y_axis(),
            rx.recharts.graphing_tooltip(),
            rx.recharts.brush(
                data_key="name", height=30, stroke="#8884d8"
            ),
            data=data,
            sync_id="1",
            width = 600,
            height = 250,
        )
    )

def area_6():
    return rx.recharts.area_chart(
        rx.recharts.area(
            data_key="uv", stroke="#8884d8", fill="#8884d8", x_axis_id="primary", y_axis_id="left",
        ),
        rx.recharts.area(
            data_key="pv", x_axis_id="secondary", y_axis_id="right", type="monotone", stroke="#82ca9d", fill="#82ca9d"
        ),
        rx.recharts.x_axis(data_key="name", x_axis_id="primary"),
        rx.recharts.x_axis(data_key="name", x_axis_id="secondary", orientation="top"),
        rx.recharts.y_axis(data_key="uv", y_axis_id="left"),
        # rx.recharts.y_axis(data_key="pv", y_axis_id="right", orientation="right"),
        rx.recharts.graphing_tooltip(),
        rx.recharts.legend(),
        data=data,
        width = 600,
        height = 300,
    )

def intro():
    return rx.text_area(
        value= """
area_1: weight, height, area.stroke, area.fill, area.type_, GraphingToolTip
area_2: margin, stack_offset, 
area_3: range_area graph
area_4, state
        """,
        width = 500,
        height = 100,
    )

def show():
    return rx.vstack(
        # intro(),
        area_1(),
        area_2(),
        area_3(),
        area_4(),
        area_5(),
        area_6(),
    )