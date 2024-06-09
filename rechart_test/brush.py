
import reflex as rx

data = [
    {"name": "1", "uv": 300, "pv": 456},
    {"name": "2", "uv": -145, "pv": 230},
    {"name": "3", "uv": -100, "pv": 345},
    {"name": "4", "uv": -8, "pv": 450},
    {"name": "5", "uv": 100, "pv": 321},
    {"name": "6", "uv": 9, "pv": 235},
    {"name": "7", "uv": 53, "pv": 267},
    {"name": "8", "uv": 252, "pv": -378},
    {"name": "9", "uv": 79, "pv": -210},
    {"name": "10", "uv": 294, "pv": -23},
    {"name": "12", "uv": 43, "pv": 45},
    {"name": "13", "uv": -74, "pv": 90},
    {"name": "14", "uv": -71, "pv": 130},
    {"name": "15", "uv": -117, "pv": 11},
    {"name": "16", "uv": -186, "pv": 107},
    {"name": "17", "uv": -16, "pv": 926},
    {"name": "18", "uv": -125, "pv": 653},
    {"name": "19", "uv": 222, "pv": 366},
    {"name": "20", "uv": 372, "pv": 486},
    {"name": "21", "uv": 182, "pv": 512},
    {"name": "22", "uv": 164, "pv": 302},
    {"name": "23", "uv": 316, "pv": 425},
    {"name": "24", "uv": 131, "pv": 467},
    {"name": "25", "uv": 291, "pv": -190},
    {"name": "26", "uv": -47, "pv": 194},
    {"name": "27", "uv": -415, "pv": 371},
    {"name": "28", "uv": -182, "pv": 376},
    {"name": "29", "uv": -93, "pv": 295},
    {"name": "30", "uv": -99, "pv": 322},
    {"name": "31", "uv": -52, "pv": 246},
    {"name": "32", "uv": 154, "pv": 33},
    {"name": "33", "uv": 205, "pv": 354},
    {"name": "34", "uv": 70, "pv": 258},
    {"name": "35", "uv": -25, "pv": 359},
    {"name": "36", "uv": -59, "pv": 192},
    {"name": "37", "uv": -63, "pv": 464},
    {"name": "38", "uv": -91, "pv": -2},
    {"name": "39", "uv": -66, "pv": 154},
    {"name": "40", "uv": -50, "pv": 186},
]

def brush_1():
    return rx.recharts.bar_chart(
        rx.recharts.bar(
            data_key="uv", stroke="#8884d8", fill="#8884d8"
        ),
        rx.recharts.bar(
            data_key="pv", stroke="#82ca9d", fill="#82ca9d"
        ),
        rx.recharts.brush(
            data_key="name", height=30, stroke="#8884d8"
        ),
        rx.recharts.x_axis(data_key="name"),
        rx.recharts.y_axis(),
        data=data,
        height = 200,
        width = 500
    )
# Explanation: This example showcases the usage of the rx.recharts.brush component in a bar chart. The brush is positioned at x=50 and y=10 with a width of 400 pixels and a height of 30 pixels. The stroke color is set to "#8884d8", and the traveller width is 15 pixels. The gap prop is set to 5, indicating the gap between the refreshing of the chart. The start_index and end_index props are set to 3 and 10, respectively, defining the default range of the brush.
def brush_2():
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
        rx.recharts.brush(
            data_key="name",
            height=20,
            stroke="#82ca9d",
            x=100,
            y=150,
            width=300,
            traveller_width=10,
            data=data[5:25],
        ),
        rx.recharts.x_axis(data_key="name"),
        rx.recharts.y_axis(),
        data=data,
        width=500,
        height=200,
    )

# Explanation: This example demonstrates the usage of the data prop in the rx.recharts.brush component. The brush is positioned at x=100 and y=150 with a width of 300 pixels and a height of 20 pixels. The stroke color is set to "#82ca9d", and the traveller width is 10 pixels. The data prop is set to a subset of the original data (data[5:25]), limiting the brush's range to a specific domain.
def brush_3():
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
        rx.recharts.brush(
            data_key="name",
            height=25,
            stroke="#ff7300",
            y=160,
            width=450,
            traveller_width=12,
            gap=10,
            start_index=0,
            end_index=30,
        ),
        rx.recharts.x_axis(data_key="name"),
        rx.recharts.y_axis(),
        data=data,
        width=500,
        height=200,
    )

def show():
    return rx.vstack(
        brush_1(),
        brush_2(),
        brush_3(),
    )