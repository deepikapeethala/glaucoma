import streamlit as st
import streamlit.components.v1 as components


# Set page title
st.set_page_config(
    page_title="Glaucoma Detection | We are...",
    initial_sidebar_state="expanded",
)
st.markdown(""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
img{border-radius: 10px;}
</style> """, unsafe_allow_html=True)
st.write('<style>div.row-widget.stMarkdown { font-size: 24px; }</style>', unsafe_allow_html=True)



st.markdown("## Glaucoma Detection & classifier")
st.write("Glaucoma is a group of eye conditions that can result in irreversible blindness if not detected and managed in its early stages. Often referred to as the "silent thief of sight," glaucoma typically progresses slowly and may not present noticeable symptoms until significant vision loss occurs. Therefore, early detection and timely intervention are crucial to preserving vision and preventing further damage.")


