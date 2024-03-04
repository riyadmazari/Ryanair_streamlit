import streamlit as st


def render_creators():

    st.markdown(""" 
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
        <link rel="stylesheet" href="../css/style.css">
        <link href='https://fonts.googleapis.com/css?family=Allerta Stencil' rel='stylesheet'>
    <style>
            h1{font-display: aligncenter;
                font-family: 'Allerta Stencil';
                color: white;}
    </style>
    <h1><center>Ozone Creators</center></h1>
    </head>
    </html>
    """, unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.subheader('Riyad Mazari')
        st.image('imgs/riyad.jpeg')
    with col2:
        st.subheader('Marouane Mrabtei')
        st.image('imgs/marouane.jpeg')
    with col3:
        st.subheader('Louis Golding')
        st.image('imgs/louis.jpeg')
    with col4:
        st.subheader('Adnan Bhanji')
        st.image('imgs/adnan.jpeg')