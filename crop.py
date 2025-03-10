# Function to fetch crop details
def get_crop_details(crop_name):
    return crops.get(crop_name, {})

# Function to display crop information
def display_crop_info(crop_name):
    crop = get_crop_details(crop_name)
    if crop:
        st.markdown(f'<img src="{crop["image"]}" style="width:100%; max-height:400px; object-fit:cover;">', unsafe_allow_html=True)

        st.markdown(f"## 🌱 {crop_name} Cultivation Process")
        st.markdown(f"**🔹 Optimal Planting Period:** {crop['optimal_period']}")
        st.markdown(f"**🔹 Water Requirement:** {crop['water_requirement']}")
        st.markdown(f"**🔹 Suitable Soil Type:** {crop['soil_type']}")
        st.markdown(f"**🔹 Cultivation Steps:** {crop['process']}")

# Function to display past history
def display_past_history(crop_name):
    crop = get_crop_details(crop_name)
    if crop:
        st.markdown(f"## 📜 Past History of {crop_name} Cultivation")
        
        history_data = {
            "Category": ["Rotation Crops", "Soil Health", "Water Management"],
            "Details": [', '.join(crop['rotation_strategies']), crop['soil_health'], crop['water_management']]
        }
        st.dataframe(history_data, width=700)

# Streamlit UI with Sidebar Navigation
st.set_page_config(page_title="Smart Farming Assistant", layout="wide")

st.sidebar.title("🌾 Smart Farming Assistant")
selected_option = st.sidebar.radio("Navigation", ["Home", "Crop Details", "Past History"])

st.sidebar.markdown("### 🌍 Select a Crop")
selected_crop = st.sidebar.selectbox("Choose a crop:", list(crops.keys()))

st.sidebar.markdown("💡 Developed to support farmers with optimized cultivation practices.JAI KISAAN!  JAI JAVAAN !!")

# Page Routing
if selected_option == "Home":
    st.title("Welcome to the Smart FARMING Assistant 🚜")
    st.markdown("""
        This tool provides insights into various crops, including:
        - 🔄 CROP Rotation Strategies  
        - 🌱 Best planting periods  
        - 🌾 Suitable soil types  
        - 💧 Water management techniques  
        - 📜 Past cultivation histories  
        
        Use the sidebar navigation to explore detailed information!
    """)

elif selected_option == "Crop Details":
    if selected_crop:
        display_crop_info(selected_crop)

elif selected_option == "Past History":
    if selected_crop:
        display_past_history(selected_crop)


