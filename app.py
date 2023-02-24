import streamlit as st

st.title(':red[Innomatics] :blue[Data] :green[App]')

st.subheader('About Me:sunglasses:')

st.text('I am Harshit Raizada.')
st.text('I am a Data Science Intern at Innomatics Research Labs.')
st.text('I am a pre-final year student pursuing a bachelors degree in Technology with a specialisation in Machine Learning & Artificial Intelligence.') 
st.text('I have a keen interest in working within the Machine Learning domain. The programming language I have a strong hold on is Python.') 
st.text('I am an initiative taker and demonstrate quick concept-grasping skills')

btn = st.button('Connect with me on LinkedIn')
if btn == True:
    st.write('https://www.linkedin.com/in/harshit-raizada/')
    st.balloons()

btn1 = st.button('Link to GitHub')
if btn1 == True:
    st.write('https://github.com/harshit-raizada')
    st.snow()