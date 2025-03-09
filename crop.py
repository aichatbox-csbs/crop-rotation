import streamlit as st
import pandas as pd

# Load dataset
@st.cache_data
def load_data():
    df = pd.read_csv('Crop_recommendation.csv')
    return df

df = load_data()

# Crop Rotation Data
crop_rotation_map = {
    'rice': ['lentil', 'chickpea', 'mustard'], 'maize': ['soybean', 'blackgram', 'pea'],
    'wheat': ['mustard', 'pea', 'sunflower'], 'cotton': ['groundnut', 'pigeon peas', 'jowar'],
    'sugarcane': ['barley', 'lentil', 'green gram'], 'carrot': ['onion', 'beetroot', 'radish'],
    'beetroot': ['cabbage', 'cauliflower', 'garlic'], 'watermelon': ['pumpkin', 'tomato', 'cucumber'],
    'tomato': ['beans', 'cabbage', 'coriander'], 'onion': ['tomato', 'carrot', 'potato'],
    'garlic': ['peas', 'mustard', 'lentil'], 'cabbage': ['tomato', 'carrot', 'radish'],
    'cauliflower': ['onion', 'spinach', 'lettuce'], 'pumpkin': ['beans', 'okra', 'peas'],
    'chickpea': ['maize', 'millet', 'sorghum'], 'blackgram': ['rice', 'maize', 'sesame'],
    'lentil': ['rice', 'mustard', 'cotton'], 'pigeon peas': ['groundnut', 'pearl millet'],
    'soybean': ['maize', 'barley', 'jowar'], 'mustard': ['wheat', 'barley', 'green gram'],
    'groundnut': ['pigeon peas', 'castor', 'sunflower'], 'peas': ['carrot', 'potato', 'cabbage'],
    'potato': ['wheat', 'maize', 'mustard'], 'sunflower': ['mustard', 'wheat', 'barley'],
    'mango': ['legumes', 'turmeric', 'ginger'], 'banana': ['legumes', 'coconut', 'pineapple'],
    'apple': ['walnut', 'pear', 'cherry'], 'grapes': ['citrus', 'olive', 'pomegranate'],
    'papaya': ['banana', 'mango', 'coconut'], 'coconut': ['pineapple', 'banana', 'mango'],
    'coffee': ['tea', 'cardamom', 'black pepper'], 'tea': ['coffee', 'black pepper', 'ginger'],
    'cashew': ['mango', 'coconut', 'banana'], 'pomegranate': ['grapes', 'guava', 'citrus'],
    'guava': ['pomegranate', 'papaya', 'lemon'], 'orange': ['lemon', 'grapefruit', 'pomegranate'],
    'lemon': ['orange', 'papaya', 'coconut'], 'jackfruit': ['banana', 'coconut', 'areca nut'],
    'areca nut': ['black pepper', 'coffee', 'cardamom'], 'black pepper': ['coffee', 'coconut', 'areca nut'],
    'muskmelon': ['pumpkin', 'cucumber', 'okra'], 'mothbeans': ['millet', 'sorghum', 'green gram'],
    'mungbean': ['maize', 'pigeon peas', 'sesame']
}

def get_crop_info(crop):
    return f"### {crop} Cultivation Process\n\n- Proper soil preparation\n- Recommended fertilizers\n- Pest control methods\n- Ideal irrigation techniques"

def get_soil_health_tips():
    return "### Soil Health Enhancement\n\n- Rotate crops regularly\n- Use compost and organic matter\n- Reduce chemical fertilizers\n- Implement cover cropping"

def get_water_management_tips():
    return "### Water Management Techniques\n\n- Use rainwater harvesting\n- Adopt drip irrigation\n- Implement mulching to retain soil moisture\n- Schedule irrigation based on soil moisture levels"

def get_past_history_table():
    return df[['label', 'N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']].head(10)

st.title("🌾 Smart Agriculture Advisory System")
st.sidebar.title("Navigation")
option = st.sidebar.selectbox("Select an Option", ["Select Crop", "Crop Rotation Strategy", "Soil Health", "Water Management Techniques", "Past History"])

if option == "Select Crop":
    crop = st.selectbox("Choose a Crop", df['label'].unique())
    st.markdown(get_crop_info(crop))
    
elif option == "Crop Rotation Strategy":
    crop = st.selectbox("Choose a Crop", df['label'].unique())
    rotation = crop_rotation_map.get(crop, ["No rotation data available"])
    st.markdown(f"### Best Crop Rotation for {crop}:\n- " + "\n- ".join(rotation))
    
elif option == "Soil Health":
    st.markdown(get_soil_health_tips())
    
elif option == "Water Management Techniques":
    st.markdown(get_water_management_tips())
    
elif option == "Past History":
    st.write("### Past Crop Cultivation Data")
    st.dataframe(get_past_history_table())

st.sidebar.write("🚜 Built for farmers to enhance crop production and sustainability.")
