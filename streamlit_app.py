"""Grammar Quest, wrapped for Streamlit Community Cloud.

The quiz itself lives in index.html (single-file HTML and JavaScript app).
This wrapper serves it inside Streamlit so it can be deployed at
share.streamlit.io and opened from any device.
"""

from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Grammar Quest", page_icon="⭐", layout="wide")

# Hide Streamlit's default chrome so the quiz fills the page
st.markdown(
    """
    <style>
    #MainMenu, header, footer {visibility: hidden;}
    .block-container {padding: 0 !important; max-width: 100% !important;}
    </style>
    """,
    unsafe_allow_html=True,
)

html = Path(__file__).parent.joinpath("index.html").read_text(encoding="utf-8")
components.html(html, height=1050, scrolling=True)
