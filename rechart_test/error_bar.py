import reflex as rx

data = [
    {
        "x": 45,
        "y": 100,
        "z": 150,
        "errorY": [30, 20],
        "errorX": 5,
    },
    {
        "x": 100,
        "y": 200,
        "z": 200,
        "errorY": [20, 30],
        "errorX": 3,
    },
    {
        "x": 120,
        "y": 100,
        "z": 260,
        "errorY": 20,
        "errorX": [5, 3],
    },
    {
        "x": 170,
        "y": 300,
        "z": 400,
        "errorY": [15, 18],
        "errorX": 4,
    },
    {
        "x": 140,
        "y": 250,
        "z": 280,
        "errorY": 23,
        "errorX": [6, 7],
    },
    {
        "x": 150,
        "y": 400,
        "z": 500,
        "errorY": [21, 10],
        "errorX": 4,
    },
    {
        "x": 110,
        "y": 280,
        "z": 200,
        "errorY": 21,
        "errorX": [5, 6],
    },
]

def show():
    return rx.recharts.scatter_chart(
        rx.recharts.scatter(
            rx.recharts.error_bar(
                data_key="errorY",
                direction="y",
                width=4,
                stroke_width=2,
                stroke="red",
            ),
            rx.recharts.error_bar(
                data_key="errorX",
                direction="x",
                width=4,
                stroke_width=2,
            ),
            data=data,
            fill="#8884d8",
            name="A",
        ),
        rx.recharts.x_axis(data_key="x", name="x"),
        rx.recharts.y_axis(data_key="y", name="y"),
        rx.recharts.graphing_tooltip(),
        rx.recharts.legend(),
        height = 200,
        width = 500,
    )
