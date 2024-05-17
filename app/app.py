import base64
import streamlit as st
import numpy as np
import joblib

# Load the model
my_model = joblib.load("app/model.pkl")


st.set_page_config(page_title="Flood Prediction",
                   layout="centered",
                   page_icon="data/flood.ico")


# Define the Streamlit app
st.markdown("""
    <style>
        .title {
            text-align: center;
            font-family: Yellow peace;
            font-weight: lighter;
            color: rgba(255, 255, 255, 1);
            font-size: 2.5rem;
            padding-bottom: 20px;
        }
        .me {
            text-align: center;
            font-family: Yellow peace;
            color: rgba(94, 78, 207);
            font-size: 1 rem;
            padding: 0;
            margin: 0;
        }
        .a {
            text-align: center;
            font-family: Yellow peace;
            color: rgba(94, 78, 207);
            padding: 0;
            margin: 0;
        }

    </style>
""", unsafe_allow_html=True)
st.markdown("<h1 class='title'> 🌊 Flood Prediction </h1>", unsafe_allow_html=True)


def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


img = get_img_as_base64("./data/flood.jpg")
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image:url("data:image/png;base64,{img}");
background-size: cover;
background-position: center top;
background-repeat: no-repeat;
background-attachment: local;
}}
[data-testid="stHeader"]
{{background: rgba(0, 0, 0, 0.2);}}
{{[data-testid="stVerticalBlockBorderWrapper"]
{{background-color: rgba(0, 0, 0, 0.2); border-radius: 16px;}}
.st-ds 
{{background-color: rgba(0, 0, 0, 0.2);}}
[.data-testid="stColorBlock"]
{{background-color: rgba(0, 0, 0, 0.2);}}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

css_code = """
<style>

[data-baseweb="tab-list"] {
    background-color: rgba(0, 0, 0, 0.6); /* Beyaz renk kodu */
    color: black; /* Tab yazı rengini ayarlayın */
    border-radius: 5px;
    padding: 10px;
}
</style>
"""
st.markdown(css_code, unsafe_allow_html=True)




# Sayfa Düzenine Tabların Eklenmesi
taba, tabb, tabc, tabd, tabe, tabf, tabg, tabh, tab1, tab2, tab3 = st.tabs(["____", "____", "____", "____", "____",
                                                                            "____", "____", "____",
                                                                            "🌍 Geographical Features",
                                                                            "🏗️️ Technical Specifications",
                                                                            "❔ Prediction"])
with tab1:
    col1, col2 = st.columns(2)
    with col1:
        MonsoonIntensity = st.slider("Monsoon Intensity", min_value=0, max_value=16, step=1)
        TopographyDrainage = st.number_input("Topography Drainage", min_value=0, max_value=18, step=1)
        Deforestation = st.number_input("Deforestation", min_value=0, max_value=17, step=1)
        ClimateChange = st.number_input("Climate Change", min_value=0, max_value=17, step=1)

    with col2:
        Encroachments = st.slider("Encroachments", min_value=0, max_value=18, step=1)
        CoastalVulnerability = st.number_input("Coastal Vulnerability", min_value=0, max_value=17, step=1)
        Landslides = st.number_input("Landslides", min_value=0, max_value=16, step=1)
        Watersheds = st.number_input("Watersheds", min_value=0, max_value=16, step=1)

    WetlandLoss = st.slider("Wetland Loss", min_value=0, max_value=22, step=1)
    Siltation = st.slider("Siltation", min_value=0, max_value=16, step=1)
with tab2:
    col3, col4 = st.columns(2)
    with col3:
        RiverManagement = st.slider("River Management", min_value=0, max_value=16, step=1)
        Urbanization = st.slider("Urbanization", min_value=0, max_value=17, step=1)
        DamsQuality = st.slider("Dams Quality", min_value=0, max_value=16, step=1)
        AgriculturalPractices = st.slider("Agricultural Practices", min_value=0, max_value=16, step=1)
        IneffectiveDisasterPreparedness = st.slider("Ineffective Disaster Preparedness", min_value=0,
                                                    max_value=16, step=1)
    with col4:
        DrainageSystems = st.slider("Drainage Systems", min_value=0, max_value=17, step=1)
        DeterioratingInfrastructure = st.slider("Deteriorating Infrastructure", min_value=0, max_value=17, step=1)
        PopulationScore = st.slider("Population Score", min_value=0, max_value=19, step=1)

        InadequatePlanning = st.slider("Inadequate Planning", min_value=0, max_value=16, step=1)
        PoliticalFactors = st.slider("Political Factors", min_value=0, max_value=16, step=1)

    with tab3:
        if st.button("Predict"):
            # Create the feature array for prediction
            X = np.array([
                MonsoonIntensity,
                TopographyDrainage,
                RiverManagement,
                Deforestation,
                Urbanization,
                ClimateChange,
                DamsQuality,
                Siltation,
                AgriculturalPractices,
                Encroachments,
                IneffectiveDisasterPreparedness,
                DrainageSystems,
                CoastalVulnerability,
                Landslides,
                Watersheds,
                DeterioratingInfrastructure,
                PopulationScore,
                WetlandLoss,
                InadequatePlanning,
                PoliticalFactors
            ]).reshape(1, -1)

            # Make prediction
            prediction = my_model.predict(X)

            # Display the prediction
            st.success(f"Flood Risk as a Percentage: {prediction[0]:.2f}")
