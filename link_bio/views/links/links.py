import reflex as rx
from link_bio.components.link_button import link_button



def links() -> rx.Component:
    return rx.vstack(
        link_button("Google", "https://www.google.com"),
        link_button("Facebook", "https://www.facebook.com"),
        link_button("Twitter", "https://www.twitter.com"),
        link_button("Instagram", "https://www.instagram.com"),
        
    )