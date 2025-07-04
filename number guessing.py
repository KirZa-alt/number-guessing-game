import random as rd
import streamlit as st

page_bg_img=f"""
<style>

.st-emotion-cache-1yiq2ps {{
    background-image: url("https://img.freepik.com/free-psd/3d-rendering-questions-background_23-2151455632.jpg?semt=ais_hybrid&w=740");
    background-size: cover;
     background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

st.markdown(
    '''
    <h2 style="
        color: DarkPurple;
        font-weight: bolder;
        font-family: 'Times New Roman', serif;;
        text-shadow:
            -1px -1px 0 white,
             1px -1px 0 white,
            -1px  1px 0 white,
             1px  1px 0 white;
    ">
        🎯 NUMBER GUESSING GAME
    </h2>
    ''',
    unsafe_allow_html=True
)



random_num = rd.randint(0, 10)

st.markdown("""
    <style>
    input[type="text"] {
        color: black !important;
        background-color: white !important; 
        border: 1px solid white;
    }
    </style>
""", unsafe_allow_html=True)



num = st.text_input("Enter a number between 0 and 10:")

if num:
    if num.isdigit():
        guess = int(num)
        if guess == random_num:
            st.success("✅ Correct, You Win!")
        else:
            st.error(f"❌ Incorrect, You fail. The number was {random_num}.")
    else:
        st.warning("⚠️ Please enter a valid number.")
