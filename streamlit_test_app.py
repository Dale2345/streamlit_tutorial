#!pip install StreamLit

import streamlit as st
import time
import pandas as pd
import numpy as np


# Display Text With StreamLit
st.title("this is the app title")
st.header("this is the markdown")
st.markdown("this is the header")
st.subheader("this is the subheader")
st.caption("this is the caption")
st.code("x=2021")
st.latex(r''' a+a r^1+a r^2+a r^3 ''')
table_data = {'Column 1': [1, 2], 'Column 2': [3, 4]}
st.write(pd.DataFrame(data=table_data))


# Display an Image

st.image("https://lh3.googleusercontent.com/yuUrDV2DAtBRvItHZ2FvXMkPbHR5NEt4kXbpp8dgK-r9jI9-irP19GJb2CvdBRYmy41KG4BxFu2Hod9GzdgGc46iYmm7As4bNNsc-JP7vYwY8d1BzHgZdvKR7H4xtLM20zR9gn0PJE-nQU0navp9Xh0pHc3Cp-CjYUENN7dWZ3NJiw8CiHFEJn7Mc0ul_A")


# Streamlit Widgets

st.checkbox('yes')
#st.button('Click')
st.radio('Pick your gender', ['Male', 'Female'])
st.selectbox('Pick your gender', ['Male', 'Female'])
st.multiselect('choose a planet', ['Jupiter', 'Mars', 'neptune'])
st.select_slider('Pick a mark', ['Bad', 'Good', 'Excellent'])
st.slider('Pick a number', 0, 50)


st.number_input('Pick a number', 0,10)
st.text_input('Email address')
st.date_input('Travelling date')
st.time_input('School time')
st.text_area('Description')
st.file_uploader('Upload a photo')
st.color_picker('Choose your favorite color')

#DISPLAY PROGRESS AND STATUS WITH STREAMLIT
st.balloons()
st.progress(10)
with st.spinner('Wait for it...'):
    time.sleep(10)


st.success("You did it !")
st.error("Error")
st.warning("Warning")
st.info("It's easy to build a streamlit app")
st.exception(RuntimeError("RuntimeError exception"))

#Sidebar
st.sidebar.title("This is within a Sidebar")
st.sidebar.button("Click")
st.sidebar.radio("Gender",["M","F"])

#Container
container = st.container()
container.write("This is inside a container")
