import streamlit as st
st.title("First app in Streamlit")
st.title("Simple Calculator \n")

num1 = st.text_input("Enter First Number:")
num2 = st.text_input("Enter Second Number:")
operation = st.text_input("Enter operation (+, -, *, /):")

if num1 and num2 and operation:
    try:
        n1 = float(num1)
        n2 = float(num2)

        if operation == "+":
            st.success(f"Result: {n1 + n2}")
        elif operation == "-":
            st.success(f"Result: {n1 - n2}")
        elif operation == "*":
            st.success(f"Result: {n1 * n2}")
        elif operation == "/":
            if n2 != 0:
                st.success(f"Result: {n1 / n2}")
            else:
                st.error("Cannot divide by zero.")
        else:
            st.error("Invalid operation.")
    except ValueError:
        st.error("Please enter valid numbers.")
