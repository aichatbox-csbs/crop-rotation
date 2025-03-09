import streamlit as st

# Define crop data with images
crops = {
    'Rice': {
        'image': 'https://upload.wikimedia.org/wikipedia/commons/6/62/Rice_Paddy.JPG',
        'process': 'Land preparation, transplanting seedlings, water management, harvesting.',
        'optimal_period': 'June to November',
        'soil_type': 'Clayey soil with good water retention',
        'rotation_strategies': ['Lentil', 'Chickpea', 'Mustard'],
        'soil_health': 'Incorporate green manure crops like Sesbania to enhance nitrogen content.',
        'water_management': 'Maintain 5 cm of standing water during vegetative growth.',
        'water_requirement': '450-700 mm'
    },
    'Wheat': {
        'image': 'https://upload.wikimedia.org/wikipedia/commons/9/94/Wheat_close-up.JPG',
        'process': 'Soil tillage, sowing seeds, irrigation, and harvesting.',
        'optimal_period': 'November to April',
        'soil_type': 'Well-drained loamy soil',
        'rotation_strategies': ['Mustard', 'Pea', 'Sunflower'],
        'soil_health': 'Rotate with legumes to improve soil fertility.',
        'water_management': 'Irrigate at crown root initiation, tillering, flowering, and grain filling stages.',
        'water_requirement': '400-500 mm'
    },
    'Maize': {
        'image': 'https://upload.wikimedia.org/wikipedia/commons/4/4c/Maize_field.jpg',
        'process': 'Field preparation, seed sowing, irrigation, weeding, harvesting.',
        'optimal_period': 'June to September',
        'soil_type': 'Loamy soil with good drainage',
        'rotation_strategies': ['Legumes', 'Mustard'],
        'soil_health': 'Enhance organic matter by using compost.',
        'water_management': 'Irrigate at critical growth stages: silking and grain filling.',
        'water_requirement': '500-800 mm'
    },
    'Cotton': {
        'image': 'https://upload.wikimedia.org/wikipedia/commons/7/7d/CottonPlant.jpg',
        'process': 'Seed sowing, thinning, weeding, fertilization, and harvesting.',
        'optimal_period': 'April to September',
        'soil_type': 'Loamy soil with good drainage',
        'rotation_strategies': ['Groundnut', 'Soybean', 'Maize'],
        'soil_health': 'Incorporate organic matter to maintain soil structure.',
        'water_management': 'Requires regular irrigation, especially during flowering and boll formation.',
        'water_requirement': '700-1300 mm'
    },
    'Sugarcane': {
        'image': 'https://upload.wikimedia.org/wikipedia/commons/9/9c/Sugarcane_field.jpg',
        'process': 'Land preparation, sett planting, fertilization, irrigation, and harvesting.',
        'optimal_period': 'October to March',
        'soil_type': 'Deep, well-drained loamy soil',
        'rotation_strategies': ['Pulses', 'Vegetables', 'Legumes'],
        'soil_health': 'Use trash mulching to conserve moisture and improve organic matter.',
        'water_management': 'Requires frequent irrigation; avoid waterlogging.',
        'water_requirement': '1500-2500 mm'
    },
    'Carrot': {
        'image': 'https://upload.wikimedia.org/wikipedia/commons/3/3d/Carrots_in_dirt.jpg',
        'process': 'Seed sowing, thinning, weeding, and harvesting.',
        'optimal_period': 'October to December',
        'soil_type': 'Loose, sandy loam soil',
        'rotation_strategies': ['Onions', 'Garlic', 'Tomato'],
        'soil_health': 'Maintain soil pH between 6.0 and 6.8 for optimal growth.',
        'water_management': 'Keep soil consistently moist; avoid waterlogging.',
        'water_requirement': '350-500 mm'
    },
    'Mango': {
        'image': 'https://upload.wikimedia.org/wikipedia/commons/e/e1/Mangoes_hanging_from_tree.jpg',
        'process': 'Planting saplings, pruning, pest control, and harvesting.',
        'optimal_period': 'June to July',
        'soil_type': 'Well-drained loamy soil',
        'rotation_strategies': ['Banana', 'Papaya', 'Guava'],
        'soil_health': 'Use organic compost for better fruit yield.',
        'water_management': 'Requires deep watering during dry spells.',
        'water_requirement': '700-1200 mm'
    },
    'Banana': {
        'image': 'https://upload.wikimedia.org/wikipedia/commons/4/4c/Banana_plantation.jpg',
        'process': 'Suckers planting, fertilization, irrigation, and harvesting.',
        'optimal_period': 'Throughout the year in tropical climates',
        'soil_type': 'Well-drained fertile soil with high organic content',
        'rotation_strategies': ['Sugarcane', 'Legumes', 'Vegetables'],
        'soil_health': 'Use organic mulch to retain moisture and nutrients.',
        'water_management': 'Requires frequent irrigation and humid conditions.',
        'water_requirement': '1200-2500 mm'
    },
    'Apple': {
        'image': 'https://upload.wikimedia.org/wikipedia/commons/1/15/Apple_Tree.jpg',
        'process': 'Grafting, pruning, pest control, and harvesting.',
        'optimal_period': 'December to February (Temperate regions)',
        'soil_type': 'Well-drained loamy soil',
        'rotation_strategies': ['Peas', 'Lettuce', 'Strawberries'],
        'soil_health': 'Use organic compost to maintain soil fertility.',
        'water_management': 'Requires deep watering during dry periods.',
        'water_requirement': '600-900 mm'
    },
    'Tea': {
        'image': 'https://upload.wikimedia.org/wikipedia/commons/8/86/Tea_plantation.jpg',
        'process': 'Bush planting, pruning, fertilization, and harvesting.',
        'optimal_period': 'Throughout the year in tropical regions',
        'soil_type': 'Well-drained acidic soil',
        'rotation_strategies': ['Coffee', 'Spices', 'Coconut'],
        'soil_health': 'Use organic manure to maintain soil acidity.',
        'water_management': 'Requires frequent rainfall or irrigation.',
        'water_requirement': '1500-2500 mm'
    },
    'Coffee': {
        'image': 'https://upload.wikimedia.org/wikipedia/commons/4/47/Coffee_beans_on_branch.jpg',
        'process': 'Seed planting, pruning, fertilization, and harvesting.',
        'optimal_period': 'June to September (depending on variety)',
        'soil_type': 'Well-drained loamy soil with good organic content',
        'rotation_strategies': ['Banana', 'Pepper', 'Cardamom'],
        'soil_health': 'Use shade trees to maintain soil moisture.',
        'water_management': 'Requires adequate irrigation during flowering.',
        'water_requirement': '1200-2000 mm'
    },
    'Beetroot': {
        'image': 'https://upload.wikimedia.org/wikipedia/commons/7/71/Beetroots.jpg',
        'process': 'Seed sowing, thinning, fertilization, irrigation, and harvesting.',
        'optimal_period': 'October to March',
        'soil_type': 'Well-drained sandy loam soil',
        'rotation_strategies': ['Carrot', 'Onion', 'Lettuce'],
        'soil_health': 'Use compost to maintain soil fertility and structure.',
        'water_management': 'Keep soil consistently moist; avoid waterlogging.',
        'water_requirement': '350-500 mm'
    },
    'Watermelon': {
        'image': 'https://upload.wikimedia.org/wikipedia/commons/e/ea/Watermelon.jpg',
        'process': 'Seed sowing, vine management, fertilization, irrigation, and harvesting.',
        'optimal_period': 'February to June',
        'soil_type': 'Sandy loam soil with good drainage',
        'rotation_strategies': ['Cucumber', 'Pumpkin', 'Maize'],
        'soil_health': 'Apply organic mulch to retain moisture.',
        'water_management': 'Needs frequent irrigation during fruit development.',
        'water_requirement': '400-600 mm'
    },
    'Tomato': {
        'image': 'https://upload.wikimedia.org/wikipedia/commons/8/89/Tomato_je.jpg',
        'process': 'Seedling transplanting, staking, pruning, fertilization, and harvesting.',
        'optimal_period': 'August to December',
        'soil_type': 'Loamy soil with good drainage',
        'rotation_strategies': ['Onion', 'Garlic', 'Legumes'],
        'soil_health': 'Use compost and mulch for better root health.',
        'water_management': 'Regular watering to maintain even soil moisture.',
        'water_requirement': '500-800 mm'
    },
    'Onion': {
        'image': 'https://upload.wikimedia.org/wikipedia/commons/c/c9/Onions.jpg',
        'process': 'Seed sowing, irrigation, fertilization, and harvesting.',
        'optimal_period': 'October to March',
        'soil_type': 'Loamy or sandy soil',
        'rotation_strategies': ['Carrot', 'Lettuce', 'Beetroot'],
        'soil_health': 'Avoid excessive nitrogen to prevent delayed bulb formation.',
        'water_management': 'Regular irrigation needed during bulb development.',
        'water_requirement': '350-500 mm'
    },
    'Garlic': {
        'image': 'https://upload.wikimedia.org/wikipedia/commons/4/48/Garlic_bulbs.jpg',
        'process': 'Clove planting, irrigation, weeding, and harvesting.',
        'optimal_period': 'September to January',
        'soil_type': 'Loamy soil with good organic content',
        'rotation_strategies': ['Carrot', 'Beetroot', 'Lettuce'],
        'soil_health': 'Use organic manure for better bulb growth.',
        'water_management': 'Maintain moderate soil moisture during bulb formation.',
        'water_requirement': '300-500 mm'
    },
    'Cabbage': {
        'image': 'https://upload.wikimedia.org/wikipedia/commons/2/29/Cabbage.JPG',
        'process': 'Seedling transplanting, weeding, irrigation, and harvesting.',
        'optimal_period': 'September to February',
        'soil_type': 'Well-drained loamy soil',
        'rotation_strategies': ['Lettuce', 'Onion', 'Garlic'],
        'soil_health': 'Apply compost to enrich the soil.',
        'water_management': 'Consistent watering required during head formation.',
        'water_requirement': '400-600 mm'
    },
    'Cauliflower': {
        'image': 'https://upload.wikimedia.org/wikipedia/commons/1/1e/Cauliflower.JPG',
        'process': 'Seedling transplanting, irrigation, fertilization, and harvesting.',
        'optimal_period': 'October to February',
        'soil_type': 'Well-drained loamy soil',
        'rotation_strategies': ['Carrot', 'Onion', 'Lettuce'],
        'soil_health': 'Use compost and organic fertilizers for better yield.',
        'water_management': 'Frequent watering during head formation.',
        'water_requirement': '400-600 mm'
    },
    'Pumpkin': {
        'image': 'https://upload.wikimedia.org/wikipedia/commons/9/9f/Pumpkins.jpg',
        'process': 'Seed sowing, vine training, irrigation, and harvesting.',
        'optimal_period': 'February to June',
        'soil_type': 'Well-drained sandy loam soil',
        'rotation_strategies': ['Maize', 'Watermelon', 'Cucumber'],
        'soil_health': 'Use organic mulch to retain soil moisture.',
        'water_management': 'Regular irrigation, especially during fruit setting.',
        'water_requirement': '500-700 mm'
    },
    'Chickpea': {
        'image': 'https://upload.wikimedia.org/wikipedia/commons/3/36/Chickpea_Belgium.jpg',
        'process': 'Seed sowing, irrigation, pest control, and harvesting.',
        'optimal_period': 'October to March',
        'soil_type': 'Sandy loam to clay loam soil',
        'rotation_strategies': ['Wheat', 'Mustard', 'Sunflower'],
        'soil_health': 'Improves soil fertility by fixing nitrogen.',
        'water_management': 'Limited irrigation; mostly rainfed.',
        'water_requirement': '300-400 mm'
    },
    'Blackgram': {
        'image': 'https://upload.wikimedia.org/wikipedia/commons/8/8c/Black_Gram_%28Urad%29.JPG',
        'process': 'Seed sowing, irrigation, pest control, and harvesting.',
        'optimal_period': 'June to October',
        'soil_type': 'Loamy or clayey soil',
        'rotation_strategies': ['Wheat', 'Maize', 'Pigeon Pea'],
        'soil_health': 'Fixes nitrogen and enhances soil fertility.',
        'water_management': 'Requires minimal irrigation; mostly rainfed.',
        'water_requirement': '300-450 mm'
    },
    'Lentil': {
        'image': 'https://upload.wikimedia.org/wikipedia/commons/6/69/Lentils.jpg',
        'process': 'Seed sowing, irrigation, fertilization, and harvesting.',
        'optimal_period': 'November to April',
        'soil_type': 'Well-drained sandy loam soil',
        'rotation_strategies': ['Wheat', 'Mustard', 'Sunflower'],
        'soil_health': 'Fixes nitrogen and improves soil quality.',
        'water_management': 'Minimal irrigation required.',
        'water_requirement': '250-400 mm'
    },
    'Pigeon Peas': {
        'image': 'https://upload.wikimedia.org/wikipedia/commons/2/2f/Pigeon_Peas.JPG',
        'process': 'Seed sowing, irrigation, pruning, and harvesting.',
        'optimal_period': 'June to December',
        'soil_type': 'Loamy to sandy loam soil',
        'rotation_strategies': ['Maize', 'Wheat', 'Mustard'],
        'soil_health': 'Fixes nitrogen and improves soil structure.',
        'water_management': 'Requires minimal irrigation; mostly rainfed.',
        'water_requirement': '400-600 mm'
    },
    'Soya bean': {
        'image': 'https://upload.wikimedia.org/wikipedia/commons/5/5d/Soybeans.jpg',
        'process': 'Seed sowing, irrigation, fertilization, and harvesting.',
        'optimal_period': 'June to October',
        'soil_type': 'Well-drained loamy soil',
        'rotation_strategies': ['Maize', 'Wheat', 'Mustard'],
        'soil_health': 'Fixes nitrogen and enhances soil fertility.',
        'water_management': 'Requires moderate irrigation, especially at flowering and pod formation stages.',
        'water_requirement': '500-700 mm'
    },
    'Mustard': {
        'image': 'https://upload.wikimedia.org/wikipedia/commons/2/26/Mustard_Flower.JPG',
        'process': 'Seed sowing, irrigation, pest control, and harvesting.',
        'optimal_period': 'October to March',
        'soil_type': 'Loamy to sandy loam soil',
        'rotation_strategies': ['Wheat', 'Chickpea', 'Lentil'],
        'soil_health': 'Adds organic matter to the soil and improves fertility.',
        'water_management': 'Minimal irrigation required; mostly rainfed.',
        'water_requirement': '300-400 mm'
    },
    'Groundnut': {
        'image': 'https://upload.wikimedia.org/wikipedia/commons/3/36/Groundnut.JPG',
        'process': 'Seed sowing, weeding, irrigation, and harvesting.',
        'optimal_period': 'June to September',
        'soil_type': 'Well-drained sandy loam soil',
        'rotation_strategies': ['Maize', 'Cotton', 'Pigeon Peas'],
        'soil_health': 'Fixes nitrogen and improves soil structure.',
        'water_management': 'Requires regular irrigation during pod formation.',
        'water_requirement': '500-700 mm'
    },
    'Peas': {
        'image': 'https://upload.wikimedia.org/wikipedia/commons/5/5b/Peas_in_pods_-_studio_photo.JPG',
        'process': 'Seed sowing, irrigation, staking, and harvesting.',
        'optimal_period': 'October to February',
        'soil_type': 'Well-drained loamy soil',
        'rotation_strategies': ['Wheat', 'Mustard', 'Carrot'],
        'soil_health': 'Fixes nitrogen and improves soil fertility.',
        'water_management': 'Regular irrigation required, especially during flowering.',
        'water_requirement': '400-600 mm'
    },
    'Potato': {
        'image': 'https://upload.wikimedia.org/wikipedia/commons/8/89/Potato_-_whole_and_sliced.jpg',
        'process': 'Tuber planting, irrigation, fertilization, and harvesting.',
        'optimal_period': 'October to March',
        'soil_type': 'Well-drained sandy loam soil',
        'rotation_strategies': ['Wheat', 'Mustard', 'Peas'],
        'soil_health': 'Requires crop rotation to prevent soil exhaustion.',
        'water_management': 'Frequent irrigation required, especially during tuber formation.',
        'water_requirement': '500-700 mm'
    },
    'Sunflower': {
        'image': 'https://upload.wikimedia.org/wikipedia/commons/4/40/Sunflower_sky_backdrop.jpg',
        'process': 'Seed sowing, irrigation, fertilization, and harvesting.',
        'optimal_period': 'June to October',
        'soil_type': 'Well-drained loamy to sandy soil',
        'rotation_strategies': ['Wheat', 'Mustard', 'Lentil'],
        'soil_health': 'Deep-rooted plant improves soil aeration.',
        'water_management': 'Moderate irrigation required, especially at bud formation and flowering.',
        'water_requirement': '400-600 mm'
    },
    'Mango': {
        'image': 'https://upload.wikimedia.org/wikipedia/commons/9/90/Hapus_Amba.jpg',
        'process': 'Planting saplings, irrigation, pruning, fertilization, and harvesting.',
        'optimal_period': 'June to September (Planting), April to July (Harvesting)',
        'soil_type': 'Well-drained alluvial or loamy soil',
        'rotation_strategies': ['Papaya', 'Banana', 'Guava'],
        'soil_health': 'Deep-rooted trees improve soil structure and prevent erosion.',
        'water_management': 'Irrigation required during dry spells, especially in flowering and fruit development stages.',
        'water_requirement': '600-800 mm'
    },
    'Banana': {
        'image': 'https://upload.wikimedia.org/wikipedia/commons/4/44/Banana.jpg',
        'process': 'Rhizome planting, irrigation, fertilization, staking, and harvesting.',
        'optimal_period': 'Year-round in tropical regions',
        'soil_type': 'Well-drained loamy or sandy loam soil',
        'rotation_strategies': ['Papaya', 'Sugarcane', 'Coconut'],
        'soil_health': 'Leaves and stems decompose to enhance organic matter in soil.',
        'water_management': 'Requires frequent irrigation to maintain moisture.',
        'water_requirement': '1200-2500 mm'
    },
    'Apple': {
        'image': 'https://upload.wikimedia.org/wikipedia/commons/1/15/Red_Apple.jpg',
        'process': 'Sapling planting, irrigation, pruning, pollination, and harvesting.',
        'optimal_period': 'December to February (Planting), August to October (Harvesting)',
        'soil_type': 'Well-drained loamy soil',
        'rotation_strategies': ['Peach', 'Plum', 'Walnut'],
        'soil_health': 'Requires well-maintained soil with good organic content.',
        'water_management': 'Irrigation necessary in dry periods and during fruiting stage.',
        'water_requirement': '800-1200 mm'
    },
    'Grapes': {
        'image': 'https://upload.wikimedia.org/wikipedia/commons/2/2e/Grapes.jpg',
        'process': 'Vine propagation, irrigation, pruning, fertilization, and harvesting.',
        'optimal_period': 'January to March (Planting), April to June (Harvesting)',
        'soil_type': 'Well-drained sandy loam soil',
        'rotation_strategies': ['Pomegranate', 'Lemon', 'Papaya'],
        'soil_health': 'Trellis system improves growth and soil aeration.',
        'water_management': 'Regular irrigation required, especially during flowering and fruiting.',
        'water_requirement': '500-800 mm'
    },
    'Papaya': {
        'image': 'https://upload.wikimedia.org/wikipedia/commons/3/3b/Papaya.jpg',
        'process': 'Seed planting, irrigation, fertilization, pruning, and harvesting.',
        'optimal_period': 'February to May',
        'soil_type': 'Well-drained sandy loam soil',
        'rotation_strategies': ['Banana', 'Mango', 'Coconut'],
        'soil_health': 'Enhances soil fertility with decomposing leaves.',
        'water_management': 'Regular irrigation required, especially in dry seasons.',
        'water_requirement': '1000-2000 mm'
    },
    'Coconut': {
        'image': 'https://upload.wikimedia.org/wikipedia/commons/c/cd/Coconut.jpg',
        'process': 'Sapling planting, irrigation, fertilization, dehusking, and harvesting.',
        'optimal_period': 'June to September (Planting), Year-round harvesting',
        'soil_type': 'Well-drained sandy loam soil',
        'rotation_strategies': ['Banana', 'Papaya', 'Arecanut'],
        'soil_health': 'Leaves and husks contribute to organic matter in soil.',
        'water_management': 'Regular irrigation required, especially in hot climates.',
        'water_requirement': '1500-2500 mm'
    },
    'Coffee': {
        'image': 'https://upload.wikimedia.org/wikipedia/commons/4/45/Coffee_berries.jpg',
        'process': 'Seed planting, irrigation, pruning, fertilization, and harvesting.',
        'optimal_period': 'June to September (Planting), November to March (Harvesting)',
        'soil_type': 'Well-drained volcanic or loamy soil',
        'rotation_strategies': ['Pepper', 'Arecanut', 'Cardamom'],
        'soil_health': 'Prefers shaded areas with high organic matter.',
        'water_management': 'Requires regular irrigation, especially during flowering and fruit setting.',
        'water_requirement': '1500-2500 mm'
    },
    'Tea': {
        'image': 'https://upload.wikimedia.org/wikipedia/commons/9/9b/Tea_plantation.jpg',
        'process': 'Seedling planting, irrigation, pruning, plucking, and processing.',
        'optimal_period': 'June to September (Planting), Year-round harvesting',
        'soil_type': 'Well-drained acidic loamy soil',
        'rotation_strategies': ['Arecanut', 'Coconut', 'Pepper'],
        'soil_health': 'Requires mulching and regular pruning for soil conservation.',
        'water_management': 'Regular watering required, particularly during dry seasons.',
        'water_requirement': '2000-3000 mm'
    },
    'Cashew': {
        'image': 'https://upload.wikimedia.org/wikipedia/commons/7/7a/Cashew_nut_fruit.jpg',
        'process': 'Sapling planting, irrigation, pruning, fertilization, and harvesting.',
        'optimal_period': 'June to August (Planting), February to May (Harvesting)',
        'soil_type': 'Well-drained sandy loam soil',
        'rotation_strategies': ['Mango', 'Coconut', 'Guava'],
        'soil_health': 'Prefers well-drained soil with organic mulch.',
        'water_management': 'Minimal irrigation required except in dry periods.',
        'water_requirement': '800-1500 mm'
    },
    'Pomegranate': {
        'image': 'https://upload.wikimedia.org/wikipedia/commons/b/bb/Pomegranate_fruit.jpg',
        'process': 'Seed planting, irrigation, fertilization, pruning, and harvesting.',
        'optimal_period': 'June to August (Planting), September to February (Harvesting)',
        'soil_type': 'Well-drained sandy or loamy soil',
        'rotation_strategies': ['Grapes', 'Lemon', 'Papaya'],
        'soil_health': 'Deep-rooted trees improve soil aeration and drainage.',
        'water_management': 'Requires moderate irrigation, especially during fruit development.',
        'water_requirement': '500-800 mm'
    },
    'Guava': {
        'image': 'https://upload.wikimedia.org/wikipedia/commons/6/6e/Guava_fruit.jpg',
        'process': 'Sapling planting, irrigation, pruning, fertilization, and harvesting.',
        'optimal_period': 'June to September (Planting), August to October (Harvesting)',
        'soil_type': 'Well-drained sandy loam or clay soil',
        'rotation_strategies': ['Pomegranate', 'Banana', 'Mango'],
        'soil_health': 'Organic matter from fallen leaves improves soil fertility.',
        'water_management': 'Regular irrigation required during dry seasons.',
        'water_requirement': '1000-1500 mm'
    },
    'Orange': {
        'image': 'https://upload.wikimedia.org/wikipedia/commons/b/bb/Orange_fruit.jpg',
        'process': 'Sapling planting, irrigation, pruning, fertilization, and harvesting.',
        'optimal_period': 'June to September (Planting), October to February (Harvesting)',
        'soil_type': 'Well-drained sandy loam soil',
        'rotation_strategies': ['Lemon', 'Guava', 'Papaya'],
        'soil_health': 'Mulching improves soil moisture retention.',
        'water_management': 'Regular irrigation required, especially in flowering and fruiting stages.',
        'water_requirement': '1000-1500 mm'
    },
    'Lemon': {
        'image': 'https://upload.wikimedia.org/wikipedia/commons/2/2d/Lemon_fruit.jpg',
        'process': 'Sapling planting, irrigation, pruning, fertilization, and harvesting.',
        'optimal_period': 'June to September (Planting), November to March (Harvesting)',
        'soil_type': 'Well-drained sandy loam soil',
        'rotation_strategies': ['Orange', 'Guava', 'Pomegranate'],
        'soil_health': 'Requires proper drainage to prevent root rot.',
        'water_management': 'Regular watering required, especially during fruit-setting stages.',
        'water_requirement': '900-1200 mm'
    }
}

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

st.sidebar.markdown("💡 Developed to support farmers with optimized cultivation practices.
                         JAI KISAAN , JAI JAVAAN !!")

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
