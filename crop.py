import streamlit as st

# Custom CSS for a professional Azure-like dashboard look
st.markdown("""
    <style>
        body {
            background-color: #f4f4f4;
            font-family: Arial, sans-serif;
        }
        .main-title {
            text-align: center;
            font-size: 32px;
            color: #2c3e50;
            font-weight: bold;
            margin-bottom: 20px;
        }
        .sidebar-title {
            font-size: 22px;
            font-weight: bold;
            color: #16a085;
            margin-bottom: 10px;
        }
        .dashboard-box {
            background-color: white;
            padding: 15px;
            border-radius: 10px;
            box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
            margin-bottom: 20px;
        }
        .header {
            font-size: 20px;
            font-weight: bold;
            color: #2980b9;
            margin-top: 15px;
        }
        .subtext {
            font-size: 16px;
            color: #34495e;
        }
        .azure-theme {
            background-color: #ffffff;
            border-left: 5px solid #3498db;
            padding: 15px;
            border-radius: 8px;
            margin-bottom: 15px;
        }
    </style>
""", unsafe_allow_html=True)


# Define crop data
crops = {
    'Rice': {
        'process': 'Land preparation, transplanting seedlings, water management, harvesting.',
        'optimal_period': 'June to November',
        'soil_type': 'Clayey soil with good water retention',
        'rotation_strategies': ['Lentil', 'Chickpea', 'Mustard'],
        'soil_health': 'Incorporate green manure crops like Sesbania to enhance nitrogen content.',
        'water_management': 'Maintain 5 cm of standing water during vegetative growth.',
        'water_requirement': '450-700 mm'
    },
    'Wheat': {
        'process': 'Soil tillage, sowing seeds, irrigation, and harvesting.',
        'optimal_period': 'November to April',
        'soil_type': 'Well-drained loamy soil',
        'rotation_strategies': ['Mustard', 'Pea', 'Sunflower'],
        'soil_health': 'Rotate with legumes to improve soil fertility.',
        'water_management': 'Irrigate at crown root initiation, tillering, flowering, and grain filling stages.',
        'water_requirement': '400-500 mm'
    },
    'Maize': {
        'process': 'Land preparation, seed sowing, fertilization, and harvesting.',
        'optimal_period': 'June to October',
        'soil_type': 'Well-drained fertile soil',
        'rotation_strategies': ['Soybean', 'Blackgram', 'Pea'],
        'soil_health': 'Use cover crops like clover to prevent soil erosion.',
        'water_management': 'Ensure adequate moisture during tasseling and silking stages.',
        'water_requirement': '500-800 mm'
    },
    'Cotton': {
        'process': 'Seed sowing, thinning, weeding, fertilization, and harvesting.',
        'optimal_period': 'April to September',
        'soil_type': 'Loamy soil with good drainage',
        'rotation_strategies': ['Groundnut', 'Soybean', 'Maize'],
        'soil_health': 'Incorporate organic matter to maintain soil structure.',
        'water_management': 'Requires regular irrigation, especially during flowering and boll formation.',
        'water_requirement': '700-1300 mm'
    },
    'Sugarcane': {
        'process': 'Land preparation, sett planting, fertilization, irrigation, and harvesting.',
        'optimal_period': 'October to March',
        'soil_type': 'Deep, well-drained loamy soil',
        'rotation_strategies': ['Pulses', 'Vegetables', 'Legumes'],
        'soil_health': 'Use trash mulching to conserve moisture and improve organic matter.',
        'water_management': 'Requires frequent irrigation; avoid waterlogging.',
        'water_requirement': '1500-2500 mm'
    },
    'Carrot': {
        'process': 'Seed sowing, thinning, weeding, and harvesting.',
        'optimal_period': 'October to December',
        'soil_type': 'Loose, sandy loam soil',
        'rotation_strategies': ['Onions', 'Garlic', 'Tomato'],
        'soil_health': 'Maintain soil pH between 6.0 and 6.8 for optimal growth.',
        'water_management': 'Keep soil consistently moist; avoid waterlogging.',
        'water_requirement': '350-500 mm'
    },
    'Beetroot': {
        'process': 'Seed sowing, thinning, weeding, and harvesting.',
        'optimal_period': 'September to November',
        'soil_type': 'Well-drained loamy soil',
        'rotation_strategies': ['Cabbage', 'Lettuce', 'Onion'],
        'soil_health': 'Incorporate compost to enhance soil fertility.',
        'water_management': 'Regular watering is essential; avoid drought stress.',
        'water_requirement': '400-600 mm'
    },
    'Watermelon': {
        'process': 'Seed sowing, vine training, weeding, and harvesting.',
        'optimal_period': 'January to March',
        'soil_type': 'Sandy loam soil with good drainage',
        'rotation_strategies': ['Maize', 'Sunflower', 'Soybean'],
        'soil_health': 'Maintain soil pH between 6.0 and 7.5.',
        'water_management': 'Requires ample water during fruit development.',
        'water_requirement': '600-800 mm'
    },
    'Tomato': {
        'process': 'Seedling preparation, transplanting, staking, pruning, and harvesting.',
        'optimal_period': 'February to April',
        'soil_type': 'Well-drained sandy loam soil with rich organic matter',
        'rotation_strategies': ['Carrots', 'Onions', 'Legumes'],
        'soil_health': 'Incorporate compost to improve soil structure and fertility.',
        'water_management': 'Regular watering; avoid wetting foliage to prevent diseases.',
        'water_requirement': '400-600 mm'
    },
    'Onion': {
        'process': 'Seed sowing, transplanting, weeding, and harvesting.',
        'optimal_period': 'November to February',
        'soil_type': 'Fertile, well-drained loamy soil',
        'rotation_strategies': ['Carrots', 'Lettuce', 'Beetroot'],
        'soil_health': 'Maintain soil pH between 6.0 and 7.0.',
        'water_management': 'Consistent moisture is crucial; avoid water stress.',
        'water_requirement': '350-550 mm'
    },
    'Garlic': {
        'process': 'Clove planting, weeding, fertilization, and harvesting.',
        'optimal_period': 'October to December',
        'soil_type': 'Well-drained loamy soil with high organic matter',
        'rotation_strategies': ['Tomatoes', 'Peppers', 'Eggplant'],
        'soil_health': 'Incorporate well-rotted manure to enhance fertility.',
        'water_management': 'Regular watering; reduce moisture as bulbs mature.',
        'water_requirement': '400-600 mm'
    },
    'Cabbage': {
        'process': 'Seedling preparation, transplanting, weeding, and harvesting.',
        'optimal_period': 'September to November',
        'soil_type': 'Fertile, well-drained loamy soil',
        'rotation_strategies': ['Peas', 'Beans', 'Carrots'],
        'soil_health': 'Maintain soil pH between 6.5 and 7.5.',
        'water_management': 'Requires consistent moisture; mulch to conserve water.',
        'water_requirement': '350-500 mm'
    },
    'Cauliflower': {
        'process': 'Seedling preparation, transplanting, weeding, and harvesting.',
        'optimal_period': 'October to December',
        'soil_type': 'Well-drained loamy soil rich in organic matter',
                'rotation_strategies': ['Tomatoes', 'Lettuce', 'Carrots'],
        'soil_health': 'Use compost and organic matter to improve soil structure.',
        'water_management': 'Regular watering to keep soil moist but not waterlogged.',
        'water_requirement': '400-600 mm'
    },
    'Pumpkin': {
        'process': 'Direct seed sowing, vine training, fertilization, and harvesting.',
        'optimal_period': 'February to April',
        'soil_type': 'Well-drained sandy loam soil with rich organic matter',
        'rotation_strategies': ['Corn', 'Beans', 'Sunflowers'],
        'soil_health': 'Use mulch to retain moisture and control weeds.',
        'water_management': 'Requires frequent watering during fruit development.',
        'water_requirement': '500-800 mm'
    },
    'Chickpea': {
        'process': 'Soil preparation, direct seed sowing, weeding, and harvesting.',
        'optimal_period': 'October to November',
        'soil_type': 'Well-drained sandy loam soil',
        'rotation_strategies': ['Maize', 'Mustard', 'Wheat'],
        'soil_health': 'Fixes nitrogen in the soil, improving fertility.',
        'water_management': 'Minimal irrigation required; avoid waterlogging.',
        'water_requirement': '300-400 mm'
    },
    'Blackgram': {
        'process': 'Land preparation, seed sowing, weeding, and harvesting.',
        'optimal_period': 'June to July',
        'soil_type': 'Fertile, well-drained loamy soil',
        'rotation_strategies': ['Rice', 'Wheat', 'Maize'],
        'soil_health': 'Incorporate legume residues to improve soil nitrogen levels.',
        'water_management': 'Requires moderate watering; avoid excess moisture.',
        'water_requirement': '350-500 mm'
    },
    'Pigeon Peas': {
        'process': 'Direct seed sowing, weeding, fertilization, and harvesting.',
        'optimal_period': 'June to July',
        'soil_type': 'Well-drained sandy loam soil',
        'rotation_strategies': ['Maize', 'Wheat', 'Rice'],
        'soil_health': 'Enhances soil fertility by fixing nitrogen.',
        'water_management': 'Requires deep watering at flowering and pod formation stages.',
        'water_requirement': '500-700 mm'
    },
    'Soybean': {
        'process': 'Land preparation, seed sowing, weeding, and harvesting.',
        'optimal_period': 'June to July',
        'soil_type': 'Well-drained fertile loamy soil',
        'rotation_strategies': ['Maize', 'Wheat', 'Sunflower'],
        'soil_health': 'Fixes nitrogen in the soil, improving fertility.',
        'water_management': 'Requires consistent moisture; avoid waterlogging.',
        'water_requirement': '500-700 mm'
    },
    'Mustard': {
        'process': 'Soil tillage, direct seed sowing, fertilization, and harvesting.',
        'optimal_period': 'September to October',
        'soil_type': 'Well-drained loamy soil',
        'rotation_strategies': ['Wheat', 'Peas', 'Lentils'],
        'soil_health': 'Use organic compost to improve soil fertility.',
        'water_management': 'Requires moderate irrigation at flowering and seed formation stages.',
        'water_requirement': '350-500 mm'
    },
    'Groundnut': {
        'process': 'Land preparation, seed sowing, weeding, and harvesting.',
        'optimal_period': 'June to July',
        'soil_type': 'Sandy loam soil with good drainage',
        'rotation_strategies': ['Wheat', 'Maize', 'Pulses'],
        'soil_health': 'Incorporate crop residues to improve organic matter.',
        'water_management': 'Requires irrigation during flowering and pod development.',
        'water_requirement': '500-700 mm'
    },
    'Peas': {
        'process': 'Soil preparation, seed sowing, staking, and harvesting.',
        'optimal_period': 'October to December',
        'soil_type': 'Well-drained loamy soil',
        'rotation_strategies': ['Carrots', 'Lettuce', 'Cabbage'],
        'soil_health': 'Improves soil nitrogen content through symbiotic fixation.',
        'water_management': 'Regular watering is essential, especially during flowering.',
        'water_requirement': '350-500 mm'
    },
    'Potato': {
        'process': 'Soil tillage, seed tuber planting, earthing up, and harvesting.',
        'optimal_period': 'October to December',
        'soil_type': 'Sandy loam soil rich in organic matter',
        'rotation_strategies': ['Peas', 'Carrots', 'Cabbage'],
        'soil_health': 'Use well-rotted compost to enrich soil fertility.',
        'water_management': 'Requires frequent irrigation; avoid waterlogging.',
        'water_requirement': '500-800 mm'
    },
    'Sunflower': {
        'process': 'Seed sowing, fertilization, weeding, and harvesting.',
        'optimal_period': 'February to March',
        'soil_type': 'Well-drained loamy soil',
        'rotation_strategies': ['Wheat', 'Maize', 'Soybean'],
        'soil_health': 'Use crop residues to maintain soil organic matter.',
        'water_management': 'Requires irrigation during flowering and seed filling.',
        'water_requirement': '400-600 mm'
    }
}
# Sidebar with selection options
st.sidebar.markdown("<div class='sidebar-title'>🌱 Select a Crop</div>", unsafe_allow_html=True)
selected_crop = st.sidebar.selectbox("Choose a crop to view details:", list(crops.keys()))

# Main Dashboard Content
st.markdown("<div class='main-title'>📊 Crop Rotation Strategies & Best Practices</div>", unsafe_allow_html=True)

# Display selected crop image
crop_data = crops[selected_crop]
st.image(crop_data['image'], width=700, caption=f"{selected_crop} Field")

# Azure-Style Dashboard Layout
st.markdown(f"<div class='header'>🌾 Crop Rotation Strategies</div>", unsafe_allow_html=True)
st.markdown(f"<div class='azure-theme'><b>Best Rotation Crops:</b> {', '.join(crop_data['rotation_strategies'])}</div>", unsafe_allow_html=True)

st.markdown(f"<div class='header'>🔄 Recommended Next Crop</div>", unsafe_allow_html=True)
st.markdown(f"<div class='azure-theme'><b>Suggested Crop:</b> {crop_data['recommended_next_crop']}</div>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown(f"<div class='header'>📝 Growth Process</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='azure-theme'>{crop_data['process']}</div>", unsafe_allow_html=True)

    st.markdown(f"<div class='header'>🛑 Soil Type</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='azure-theme'>{crop_data['soil_type']}</div>", unsafe_allow_html=True)

with col2:
    st.markdown(f"<div class='header'>💧 Water Management</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='azure-theme'>{crop_data['water_management']}</div>", unsafe_allow_html=True)

    st.markdown(f"<div class='header'>🚰 Water Requirement</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='azure-theme'>{crop_data['water_requirement']}</div>", unsafe_allow_html=True)

st.markdown(f"<div class='header'>🌿 Soil Health Improvement</div>", unsafe_allow_html=True)
st.markdown(f"<div class='azure-theme'>{crop_data['soil_health']}</div>", unsafe_allow_html=True)
