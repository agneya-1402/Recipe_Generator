# Recipe Generator SAAS App 👨🏻‍🍳

Welcome to the **AI-Powered Recipe Generator**! This web app generates recipes based on user inputs like dietary preferences, meal type, cuisine, calorie limits, allergies, and available ingredients. Built using **Streamlit** and the **Gemini** API, this app provides personalized recipes tailored to your needs.

## Features

- **Dietary Preferences**: Choose between Veg, Non-Veg, or Vegan.
- **Meal Type**: Select the type of meal (Breakfast, Lunch, Dinner, Snacks).
- **Cuisine**: Choose from a variety of cuisines such as Indian, Chinese, Italian, Mexican, American, and others.
- **Calories**: Set a maximum calorie limit for the recipe.
- **Allergies**: Add allergies to exclude certain ingredients.
- **Ingredients**: Input the ingredients you already have at hand or leave it empty to discover new recipes.

## Installation

### Requirements

1. **Python 3.x** (preferably 3.8+)
2. **Streamlit**: For the web interface.
3. **Google Generative AI**: For generating recipes.

### Steps to Install

1. **Clone the repository**:

    ```bash
    git clone https://github.com/agneya-1402/Recipe_Generator.git
    cd Recipe_Generator
    ```

2. **Create a virtual environment (optional but recommended)**:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  
    ```

3. **Install required packages**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Get your API Key**:
    - Sign up for the **Google Gemini API** at [Google Cloud](https://cloud.google.com/ai) and generate an API key.
    - Replace `key` in the code with your API key.

5. **Run the app**:

    ```bash
    streamlit run app.py
    ```

6. Open your browser and visit `http://localhost:8501` to access the app.

---

## How It Works

- The app uses **Google Gemini 1.5 Flash** API to generate recipes based on user input.
- Upon selecting your dietary preferences, meal type, cuisine, and other inputs, the app creates a custom recipe.
- The recipe is displayed on the page with ingredients and cooking instructions.

## Usage

1. **Dietary Preference**: Choose between **Veg**, **Non-Veg**, or **Vegan**.
2. **Meal Type**: Select from **Breakfast**, **Lunch**, **Dinner**, or **Snacks**.
3. **Cuisine**: Choose your favorite cuisine from options like **Indian**, **Chinese**, **Italian**, etc.
4. **Calories**: Set the maximum number of calories for your recipe.
5. **Allergies**: Add any allergies (comma-separated) to exclude ingredients you're allergic to.
6. **Ingredients**: Specify any ingredients you already have (comma-separated).

After pressing the "Generate Recipe" button, the app will display a recipe suggestion based on your preferences.

---

## Example Inputs

- **Dietary Preference**: Veg
- **Meal Type**: Lunch
- **Cuisine**: Indian
- **Max Calories**: 500
- **Allergies**: Gluten, Nuts
- **Ingredients**: Rice, Lentils

---

## Future Enhancements

- **Image Generation**: Although image generation was removed for now, this feature could be re-integrated in the future.
- **Save Recipes**: Users can save their generated recipes as PDFs or text files.
- **User Profiles**: Add functionality for users to save their preferences and generate recipes easily.
- **Integration with Grocery APIs**: Automatically add missing ingredients to your grocery shopping list.

---

## Contributing

Feel free to fork this repository and submit pull requests with improvements. Contributions are always welcome!

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
