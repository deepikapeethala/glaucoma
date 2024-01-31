import streamlit as st
import streamlit.components.v1 as components

# Set page title
st.set_page_config(
    page_title="Glaucoma Detection",
    initial_sidebar_state="expanded",
)
st.write('<style>div.row-widget.stMarkdown { font-size: 24px; }</style>', unsafe_allow_html=True)

st.markdown(""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style> """, unsafe_allow_html=True)
components.html(
    """
    <style>
        #effect{
            margin:0px;
            padding:0px;
            font-family: "Source Sans Pro", sans-serif;
            font-size: max(8vw, 20px);
            font-weight: 700;
            top: 0px;
            right: 25%;
            position: fixed;
            background: -webkit-linear-gradient(0.25turn,blue,white);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        p{
            font-size: 2rem;
        }
    </style>
    <p id="effect">GlaucoCheck</p>
    """,
    height=69,
)



def page_layout():
   
    st.write("Glaucoma detection Check is an app developed by Students Of SVEC that takes an image as input and predicts whether glaucoma present or not.")
    st.write("Developed By SVEC")
    st.markdown("## Prevalence:")
    st.write("-  Glaucoma is a leading cause of irreversible blindness worldwide")
    st.write("- Non-invasive and painless diagnosis using Fundus Images")
    st.write("-  Approximately 76 million people are estimated to have glaucoma globally.")
    st.markdown("##  Impact on Vision:")
    st.write("- Glaucoma can lead to gradual peripheral vision loss, and if left untreated, it may eventually result in complete blindness.")
    st.write("- The vision loss caused by glaucoma is irreversible, but early detection and treatment can help slow down or prevent further damage.")
    st.write("- It uses advanced algorithms to provide fast and accurate diagnosis")
    st.markdown("## Impact on Quality of Life:")
    st.write("-Glaucoma can significantly impact an individual's quality of life, affecting daily activities and independence")

    
# Render page layout
page_layout()
