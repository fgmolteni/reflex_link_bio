import reflex as rx

def footer() -> rx.Component:
    return rx.vstack(
        rx.image(src="favicon.ico"),
        rx.link("Privacy Policy", href="/privacy"),
        rx.text("© 2021 Link Bio"),
    )