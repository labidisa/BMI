import streamlit as st

# Give a title to our app
st.title('Welcome to BMI Calculator')

# Take weight input in kgs
weight = st.number_input("Enter your weight (in kgs)", min_value=0.0)

# Option to choose height measurement
status = st.radio("Select height format:", ('Centimeters', 'Meters'))

# Initialize height and BMI
height = 0
bmi = None

# Take height input based on the selected format
if status == 'Centimeters':
    height = st.number_input("Enter your height (in centimeters)", min_value=0.0)
    height = height / 100  # Convert height from centimeters to meters
elif status == 'Meters':
    height = st.number_input("Enter your height (in meters)", min_value=0.0)
# Calculate BMI when button is pressed
if st.button('Calculate BMI'):
    if height > 0:
        bmi = weight / (height ** 2)
        st.text(f"Your BMI Index is {bmi:.2f}.")

        # Give the interpretation of BMI index
        if bmi < 16:
            st.error("You are Extremely Underweight")
        elif 16 <= bmi < 18.5:
            st.warning("You are Underweight")
        elif 18.5 <= bmi < 25:
            st.success("Healthy")
        elif 25 <= bmi < 30:
            st.warning("Overweight")
        else:
            st.error("Extremely Overweight")
    else:
        st.error("Please enter a valid height")