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
        "errorX": [10, 3],
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
        "errorX": [1, 8],
    },
]

def show():
    return rx.recharts.scatter_chart(
        rx.recharts.scatter(
            data=data, fill="#8884d8", name="A"
        ),
        rx.recharts.reference_area(
            x1=150,
            x2=180,
            y1=150,
            y2=300,
            fill="#8884d8",
            fill_opacity=0.3,
        ),
        rx.recharts.x_axis(
            data_key="x", name="x", type_="number"
        ),
        rx.recharts.y_axis(
            data_key="y", name="y", type_="number"
        ),
        rx.recharts.graphing_tooltip(),
        height = 200,
        width = 500,
    )