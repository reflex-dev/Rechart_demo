
import reflex as rx

data01 = [
    {"name": "Group A", "value": 400},
    {"name": "Group B", "value": 300},
    {"name": "Group C", "value": 300},
    {"name": "Group D", "value": 200},
    {"name": "Group E", "value": 278},
    {"name": "Group F", "value": 189},
] 

data02 = [
    {"name": "Group A", "value": 2400},
    {"name": "Group B", "value": 4567},
    {"name": "Group C", "value": 1398},
    {"name": "Group D", "value": 9800},
    {"name": "Group E", "value": 3908},
    {"name": "Group F", "value": 4800},
]

def pie_single():
    return rx.recharts.pie_chart(
        rx.recharts.pie(
            data=data01,
            data_key="value",
            name_key="name",
            cx="50%",
            cy="50%",
            fill="#8884d8",
            label=True,
        ),
        height = 200,
        width = 500,
    )

def pie_double():
    return rx.recharts.pie_chart(
        rx.recharts.pie(
            data=data01,
            data_key="value",
            name_key="name",
            cx="50%",
            cy="50%",
            fill="#82ca9d",
            inner_radius="60%",
        ),
        rx.recharts.pie(
            data=data02,
            data_key="value",
            name_key="name",
            cx="50%",
            cy="50%",
            fill="#8884d8",
            outer_radius="50%",
        ),
        rx.recharts.graphing_tooltip(),
        height = 200,
        width = 500,
    )

# class PieChartState(rx.State):
#     resources: list[dict[str, any]] = [
#         dict(type_="🏆", count=1),
#         dict(type_="🪵", count=1),
#         dict(type_="🥑", count=1),
#         dict(type_="🧱", count=1),
#     ]

#     @rx.cached_var
#     def resource_types(self) -> list[str]:
#         return [r["type_"] for r in self.resources]

#     def increment(self, type_: str):
#         for resource in self.resources:
#             if resource["type_"] == type_:
#                 resource["count"] += 1
#                 break

#     def decrement(self, type_: str):
#         for resource in self.resources:
#             if resource["type_"] == type_ and resource["count"] > 0:
#                 resource["count"] -= 1
#                 break

# def pie_dynamic():
#     return rx.hstack(
#     rx.recharts.pie_chart(
#         rx.recharts.pie(
#             data=PieChartState.resources,
#             data_key="count",
#             name_key="type_",
#             cx="50%",
#             cy="50%",
#             start_angle=180,
#             end_angle=0,
#             fill="#8884d8",
#             label=True,
#         ),
#         rx.recharts.graphing_tooltip(),
#     ),
#     rx.vstack(
#         rx.foreach(
#             PieChartState.resource_types,
#             lambda type_, i: rx.hstack(
#                 rx.button(
#                     "-",
#                     on_click=PieChartState.decrement(type_),
#                 ),
#                 rx.text(
#                     type_,
#                     PieChartState.resources[i]["count"],
#                 ),
#                 rx.button(
#                     "+",
#                     on_click=PieChartState.increment(type_),
#                 ),
#             ),
#         ),
#     ),
#     width="100%",
#     height="15em",
# )

def show():
    return rx.vstack(
        pie_single(),
        pie_double(),
    )