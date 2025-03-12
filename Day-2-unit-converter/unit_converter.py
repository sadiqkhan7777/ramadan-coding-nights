import streamlit as st  

def convert_units(value, unit_from, unit_to):
    conversions = {
        "meters_kilometers": 0.001,  # 1 meter = 0.001 kilometers
        "kilometers_meters": 1000,  # 1 kilometer = 1000 meters
        "grams_kilograms": 0.001,  # 1 gram = 0.001 kilograms
        "kilograms_grams": 1000,  # 1 kilogram = 1000 grams
    }

    key = f"{unit_from}_{unit_to}" 
    if key in conversions:
        conversion = conversions[key]
        
        return (
            conversion(value) if callable(conversion) else value * conversion
        )  
    else:
        return "Conversion not supported"  


# Streamlit UI setup
st.title("Simple Unit Converter By Sadiq")  # Set title for the web app

# User input: numerical value to convert
value = st.number_input("Enter value:", min_value=1.0, step=1.0)

# Dropdown to select unit to convert from
unit_from = st.selectbox(
    "Convert from:", ["meters", "kilometers", "grams", "kilograms"]
)

# Dropdown to select unit to convert to
unit_to = st.selectbox("Convert to:", ["meters", "kilometers", "grams", "kilograms"])

# Button to trigger conversion
if st.button("Convert"):
    result = convert_units(value, unit_from, unit_to)  
    st.write(f"Converted Value: {result}") 
