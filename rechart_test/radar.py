
import reflex as rx

data = [
    {
        "subject": "Math",
        "A": 120,
        "B": 110,
        "fullMark": 150,
    },
    {
        "subject": "Chinese",
        "A": 98,
        "B": 130,
        "fullMark": 150,
    },
    {
        "subject": "English",
        "A": 86,
        "B": 130,
        "fullMark": 150,
    },
    {
        "subject": "Geography",
        "A": 99,
        "B": 100,
        "fullMark": 150,
    },
    {
        "subject": "Physics",
        "A": 85,
        "B": 90,
        "fullMark": 150,
    },
    {
        "subject": "History",
        "A": 65,
        "B": 85,
        "fullMark": 150,
    },
]

def radar_single():
    return rx.recharts.radar_chart(
        rx.recharts.radar(
            data_key="A",
            stroke="#8884d8",
            fill="#8884d8",
        ),
        rx.recharts.polar_grid(),
        rx.recharts.polar_angle_axis(data_key="subject"),
        data=data,
        height = 200,
        width = 500,
    )

def radar_double():
    return rx.recharts.radar_chart(
        rx.recharts.radar(
            data_key="A",
            stroke="#8884d8",
            fill="#8884d8",
        ),
        rx.recharts.radar(
            data_key="B",
            stroke="#82ca9d",
            fill="#82ca9d",
            fill_opacity=0.6,
        ),
        rx.recharts.polar_grid(),
        rx.recharts.polar_angle_axis(data_key="subject"),
        rx.recharts.legend(),
        data=data,
        height = 200,
        width = 500,
    )

def show():
    return rx.vstack(
        radar_single(),
        radar_double(),
    )
