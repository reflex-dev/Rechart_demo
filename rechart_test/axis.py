import reflex as rx

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
    {'x': 0, 'y': 0},
    {'x': 50, 'y': 50},
    {'x': 100, 'y': 110},
    {'x': 150, 'y': 160},
    {'x': 200, 'y': 200},
    {'x': 250, 'y': 250},
    {'x': 350, 'y': 390},
    {'x': 400, 'y': 400},
    {'x': 450, 'y': 440},
    {'x': 500, 'y': 490},
    {'x': 550, 'y': 550},
    {'x': 600, 'y': 600},
    {'x': 650, 'y': 640},
    {'x': 700, 'y': 680},
    {'x': 750, 'y': 700},
    {'x': 800, 'y': 720},
]
        # on_animation_start = rx.window_alert("Amimation Start"),
        # on_animation_end = rx._x.toast("Animation end"),

# height and width are indicated how much space takes. 
def axis_1():
    return rx.recharts.area_chart(
        rx.recharts.area(
            data_key="uv", stroke="#8884d8", fill="#8884d8"
        ),
        rx.recharts.x_axis(
            data_key="name",
            on_click=rx._x.toast("X axis clicked"),
        ),
        rx.recharts.y_axis(
            on_mouse_over=rx.window_alert("mouse over Y"),
        ),
        data=data,
        width = 500,
        height = 400,
    )


def axis_2():
    return rx.recharts.line_chart(
        rx.recharts.line(
            data_key="y",
            stroke="#8884d8",
        ),
        rx.recharts.x_axis(data_key="x", tick_count = 7, min_tick_gap = 30),
        rx.recharts.y_axis(tick_line = False, ticks = [200, 300, 500, 800]),
        data=data2,
        width = 500,
        height = 400,
    )
def intro():
    return rx.text_area(
        value = """
axis_1: hide, 
        """
    )
def show():
    return rx.vstack(
        axis_1(),
        axis_2(),
    )