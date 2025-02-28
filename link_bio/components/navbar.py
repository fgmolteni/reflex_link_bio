import reflex as rx

def navbar() -> rx.Component:
    return rx.hstack(
        rx.text(
            "Gabi",
            height="40px",
            font_size="1em",
            ),
        position="sticky",
        bg="blue",
        padding_x="16px",
        padding_y="8px",
        z_index="999",

    )