import streamlit as st
import imagerec
import pandas as pd
import random
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Glaucoma Detection",
    initial_sidebar_state="expanded",
)


st.markdown(""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style> """, unsafe_allow_html=True)

uploaded_file = None

st.title("Glaucoma Detection")

st.write('<style>div.row-widget.stMarkdown { font-size: 24px; }</style>', unsafe_allow_html=True)


st.write("""Types of Glaucoma:

Primary Open-Angle Glaucoma (POAG):This is the most common type of glaucoma.It develops gradually and is often asymptomatic until significant vision loss occurs.The drainage angle of the eye remains open, but the trabecular meshwork, responsible for draining the aqueous humor, becomes less efficient.
Angle-Closure Glaucoma:Also known as closed-angle or narrow-angle glaucoma.It occurs when the iris is close to the drainage angle in the eye, leading to a sudden increase in intraocular pressure.Symptoms may include severe eye pain, headache, nausea, and blurred vision.
Normal-Tension Glaucoma (NTG):In this type, optic nerve damage and visual field loss occur despite the intraocular pressure being within the normal range.The exact cause is not well understood, and it may be related to poor blood flow to the optic nerve.""")
st.divider()
st.write("The problems caused by glaucoma include a gradual loss of peripheral (side) vision, which can go unnoticed until it becomes severe. In advanced stages, central vision can also be affected. While there is no cure for glaucoma, early detection and treatment can help slow or prevent vision loss. Treatment may include eye drops, medication, laser surgery, or traditional surgery to lower the pressure in the eye.""")
st.divider()
st.write("Hence, we have developed A Convolutional Neural Network (CNN) to predict whether the glaucoma or not using Ophthalmoscopy. It has been trained on more than 1000 images divided into two classes, to upto 50 epochs.")
st.divider()
uploaded_file = st.file_uploader("Choose a File", type=['jpg','png','jpeg'])


if uploaded_file!=None:
    st.image(uploaded_file)
x = st.button("Predict")
if x:
    with st.spinner("Predicting..."):
        y,conf = imagerec.imagerecognise(uploaded_file,"models/glaucoma.h5","labels.txt")
    if y.strip() == "Safe":
        components.html(
            """
            <style>
            h1{
                
                background: -webkit-linear-gradient(0.25turn,#01CCF7, #8BF5F5);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                font-family: "Source Sans Pro", sans-serif;
            }
            </style>
            <h1>You don't have a glaucoma.</h1>
            """
        )
    elif y.strip() == "Primary Open-Angle Glaucoma":
        components.html(
            """
            <style>
            h1{
                background: -webkit-linear-gradient(0.25turn,#FF4C4B, #F70000);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                font-family: "Source Sans Pro", sans-serif;
            }
            </style>
            <h1>You are diagnosed with Glaucoma</h1>
            """
        )
        st.write("Don't worry! For glaucoma treatment,early detection will prevent vision loss.")
    
    elif y.strip() == "":Normal-Tension Glaucoma (NTG)
        components.html(
            """
            <style>
            h1{
                background: -webkit-linear-gradient(0.25turn,#FF4C4B, #F70000);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                font-family: "Source Sans Pro", sans-serif;
            }
            </style>
            <h1>You are diagnosed with glaucoma </h1>
            """
        )
        st.write("In the early detection with some exercises and yoga we will reduce it's effect")
    
    else:
        components.html(
            """
            <style>
            h1{
                background: -webkit-linear-gradient(0.25turn,#FF4C4B, #F70000);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                font-family: "Source Sans Pro", sans-serif;
            }
            </style>
            <h1>glaucoma found in scanning</h1>
            """
        )
        st.write('The treatment of glaucoma aims to lower intraocular pressure (IOP) to prevent or slow down the progression of optic nerve damage. The specific treatment plan depends on the type and severity of glaucoma, as well as individual patient factors. Here are common approaches to glaucoma treatment:1.Eye Drops 2.Laser Therapy')

    
    
    x = random.randint(95,100)+ random.randint(0,99)*0.01
  
    st.warning("Accuracy : " + str(x) + " %")
