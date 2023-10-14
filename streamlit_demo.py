import streamlit as st
st.title('welcome to streamlit')
t=st.checkbox('I agree')
if t:
    st.write('Great!')
gender=st.radio('Select Gender:',{'Male','Female'})
if gender=='Male':
    st.success('Male')
else:
    st.success('Female')