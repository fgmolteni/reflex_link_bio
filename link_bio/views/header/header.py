import reflex as rx

def header() -> rx.Component:
    return rx.vstack(
        rx.avatar(fallback="G", size="4"),
        rx.text("@gabriel", font_size="1.5em"),
        rx.text("Software Engineer", font_size="1em"),
        rx.text("I am a software engineer with a passion for building products that make a difference."),
        
    )