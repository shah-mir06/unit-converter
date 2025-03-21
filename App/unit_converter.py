import streamlit as st

def convert_units(value, from_unit, to_unit):

    if from_unit == "meter" and to_unit == "kilometer":
        return value / 1000
    elif from_unit == "meter" and to_unit == "centimeter":
        return value * 100
    elif from_unit == "meter" and to_unit == "millimeter":
        return value * 1000
    elif from_unit == "kilometer" and to_unit == "meter":
        return value * 1000
    elif from_unit == "kilometer" and to_unit == "mile":
        return value * 0.621371

    elif from_unit == "gram" and to_unit == "kilogram":
        return value / 1000
    elif from_unit == "gram" and to_unit == "pound":
        return value * 0.00220462
    elif from_unit == "kilogram" and to_unit == "gram":
        return value * 1000
    elif from_unit == "kilogram" and to_unit == "pound":
        return value * 2.20462

    elif from_unit == "celsius" and to_unit == "fahrenheit":
        return (value * 9/5) + 32

    return None

st.title("Welcome to Unit Converter.")
st.markdown("---")
value = st.number_input("Enter value:", min_value=0.0, format="%.2f")
from_unit = st.selectbox("From Unit", ["meter", "kilometer", "gram", "kilogram", "celsius"])
to_unit = st.selectbox("To Unit", ["kilometer", "meter", "mile", "centimeter", "millimeter", "gram", "kilogram", "pound", "fahrenheit"])

if st.button("Convert"):
    result = convert_units(value, from_unit, to_unit)

    if result is not None:
        st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")
    else:
        st.error("Invalid conversion!")

st.markdown("---") 
st.markdown("**Developed by Shah Mir Usman**")

