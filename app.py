import streamlit as st

st.set_page_config(
    page_title="Paper Tape",
    layout="wide"
)

with open("Paper Tape – day-trading replay.html", "r", encoding="utf-8") as f:
    html = f.read()

html = f"""
<style>
    body {{
        zoom: 0.85;
    }}
</style>
{html}
"""

st.components.v1.html(
    html,
    height=1250,
    scrolling=True
)