import streamlit as st
import google.generativeai as genai

# Gemini Key
GEMINI_API_KEY = "key"
genai.configure(api_key=GEMINI_API_KEY)

st.title("🍽️ AI-Powered Recipe Generator")

# Inputs
diet = st.selectbox("Dietary Preference", ["Veg", "Non-Veg", "Vegan"])
meal = st.selectbox("Meal Type", ["Breakfast", "Lunch", "Dinner", "Snacks"])
cuisine = st.selectbox("Cuisine", ["Indian", "Chinese", "Italian", "Mexican", "American", "Other"])
calories = st.slider("Max Calories", 100, 1000, 500)
allergies = st.text_input("Allergies (comma-separated)")
ingredients = st.text_area("Ingredients You Have (comma-separated)")

if st.button("Generate Recipe"):
    # prompt for Gemini
    prompt = f"""
    Generate a {diet} {meal} recipe from {cuisine} cuisine within {calories} calories.
    Exclude ingredients causing these allergies: {allergies}.
    Prioritize these ingredients if possible: {ingredients}.
    Provide the recipe name, ingredients list, and cooking steps.
    """

    # get response 
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)

    # display 
    st.subheader("🍳 Suggested Recipe")
    st.write(response.text if response.text else "No recipe found. Try different inputs.")
