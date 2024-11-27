import streamlit as st
from Pages import home, project1, Project2, Project3
from streamlit_navigation_bar import st_navbar as navbar
import os
from PIL import Image
import pandas as pd
import numpy as np

image = Image.open('Image/logo.png')
st.set_page_config(initial_sidebar_state="collapsed", page_icon=image)

logo_path = os.path.join(os.path.dirname(__file__), "Image", "logo.svg")
pages = ["home", "project1", "Project2", "Project3"]

styles = {
    "nav": {
        "background-color": "#f8d7f0",
        "display": "flex",
        "justify-content": "center",
        "padding": "10px",
        "box-shadow": "0 2px 4px rgba(0, 0, 0, 0.1)"
    },
    "img": {
        "position": "absolute",
        "left": "15px",
        "top": "5px",
        "width": "90px",
        "height": "40px"
    },
    "div": {
        "max-width": "32rem"
    },
    "span": {
        "border-radius": "0.5rem",
        "display": "block",
        "color": "#000000",
        "margin": "0 0.5rem",
        "padding": "0.6rem 1.2rem",
        "font-size": "16px",
        "font-weight": "500",
        "transition": "background-color 0.3s ease-in-out, color 0.3s ease-in-out"
    },
    "active": {
        "background-color": "#ffffff",
        "color": "#000000",
        "font-weight": "bold"
    },
    "hover": {
        "background-color": "#ffffff",
        "color": "#000000"
    }
}




options = {
    "show_menu": False,
    "show_sidebar": True,
}


page = navbar(pages, styles=styles, logo_path=logo_path, options=options)

if page == "home":
    home.home().app()
elif page == "project1":
    project1.project1().app()
elif page == "Project2":
    Project2.Project2().app()
elif page == "Project3":
    Project3.Project3().app()
else:
    home.home().app()