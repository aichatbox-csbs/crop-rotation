import streamlit as st
import pandas as pd

# Load dataset
@st.cache_data
def load_data():
    return pd.read_csv('Crop_recommendation.csv')

df = load_data()

# Crop Rotation Data
crop_rotation_map = {
    'rice': ['lentil', 'chickpea', 'mustard'], 'maize': ['soybean', 'blackgram', 'pea'], 'wheat': ['mustard', 'pea', 'sunflower'],
    'cotton': ['groundnut', 'pigeon peas', 'jowar'], 'sugarcane': ['barley', 'lentil', 'green gram'], 'carrot': ['onion', 'beetroot', 'radish'],
    'beetroot': ['cabbage', 'cauliflower', 'garlic'], 'watermelon': ['pumpkin', 'tomato', 'cucumber'], 'tomato': ['beans', 'cabbage', 'coriander'],
    'onion': ['tomato', 'carrot', 'potato'], 'garlic': ['peas', 'mustard', 'lentil'], 'cabbage': ['tomato', 'carrot', 'radish'],
    'cauliflower': ['onion', 'spinach', 'lettuce'], 'pumpkin': ['beans', 'okra', 'peas'], 'chickpea': ['maize', 'millet', 'sorghum'],
    'blackgram': ['rice', 'maize', 'sesame'], 'lentil': ['rice', 'mustard', 'cotton'], 'pigeon peas': ['groundnut', 'pearl millet'],
    'soybean': ['maize', 'barley', 'jowar'], 'mustard': ['wheat', 'barley', 'green gram'], 'groundnut': ['pigeon peas', 'castor', 'sunflower'],
    'peas': ['carrot', 'potato', 'cabbage'], 'potato': ['wheat', 'maize', 'mustard'], 'sunflower': ['mustard', 'wheat', 'barley']
}

def get_crop_info(crop):
    return f"### {crop.capitalize()}\n- Suitable soil: Loamy soil with good drainage\n- Water requirement: Moderate\n- Best season: Kharif/Rabi\n- Fertilization: Organic compost and balanced NPK\n- Harvesting time: 90-120 days"

def get_soil_health_tips(crop):
    return f"### Soil Health for {crop.capitalize()}\n- Use green manure crops like legumes\n- Maintain pH balance using organic compost\n- Mulching for moisture retention and temperature control\n- Rotate crops to prevent soil depletion"

def get_water_management_tips(crop):
    tips = {
        'rice': "Flood irrigation or alternate wetting-drying method.",
        'maize': "Drip irrigation and soil moisture conservation techniques.",
        'wheat': "Sprinkler irrigation and rainwater harvesting.",
        'cotton': "Furrow irrigation and water scheduling.",
        'sugarcane': "Drip irrigation to optimize water usage.",
    }
    return f"### Water Management for {crop.capitalize()}\n- {tips.get(crop, 'Use water-saving irrigation methods like drip irrigation and mulching.')}"

st.title("🌾 Smart Agriculture Advisory")
st.sidebar.title("Navigation")
option = st.sidebar.selectbox("Select an Option", ["Select Crop", "Crop Rotation Strategy", "Soil Health", "Water Management Techniques", "Past History"])

if option == "Select Crop":
    crop = st.selectbox("Choose a Crop", df['label'].unique())
    st.write(get_crop_info(crop))
    
elif option == "Crop Rotation Strategy":
    crop = st.selectbox("Choose a Crop", df['label'].unique())
    rotation = crop_rotation_map.get(crop, ["No rotation data available"])
    st.write(f"### Best Crop Rotation for {crop.capitalize()}\n- {', '.join(rotation)}")
    
elif option == "Soil Health":
    crop = st.selectbox("Choose a Crop", df['label'].unique())
    st.write(get_soil_health_tips(crop))
    
elif option == "Water Management Techniques":
    crop = st.selectbox("Choose a Crop", df['label'].unique())
    st.write(get_water_management_tips(crop))
    
elif option == "Past History":
    crop = st.selectbox("Choose a Crop", df['label'].unique())
    past_data = {
        "Crop": crop,
        "Rotation Strategy": ', '.join(crop_rotation_map.get(crop, ['No data'])),
        "Soil Health Tips": get_soil_health_tips(crop),
        "Water Management": get_water_management_tips(crop)
    }
    st.write("### Past Crop Analysis")
    st.table(pd.DataFrame([past_data]))

st.sidebar.write("🚜 Built for farmers to enhance crop production and sustainability.")
