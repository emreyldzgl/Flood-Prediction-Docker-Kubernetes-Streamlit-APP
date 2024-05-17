import streamlit as st
import numpy as np
import joblib

# Load the model
my_model = joblib.load("app/model.pkl")

# Define the Streamlit app

st.title("Flood ML App")

st.write("Enter the values for the features below:")

# Create input fields for the user to enter data
MonsoonIntensity = st.number_input("Monsoon Intensity", min_value=0, max_value=10, step=1)
TopographyDrainage = st.number_input("Topography Drainage", min_value=0, max_value=10, step=1)
RiverManagement = st.number_input("River Management", min_value=0, max_value=10, step=1)
Deforestation = st.number_input("Deforestation", min_value=0, max_value=10, step=1)
Urbanization = st.number_input("Urbanization", min_value=0, max_value=10, step=1)
ClimateChange = st.number_input("Climate Change", min_value=0, max_value=10, step=1)
DamsQuality = st.number_input("Dams Quality", min_value=0, max_value=10, step=1)
Siltation = st.number_input("Siltation", min_value=0, max_value=10, step=1)
AgriculturalPractices = st.number_input("Agricultural Practices", min_value=0, max_value=10, step=1)
Encroachments = st.number_input("Encroachments", min_value=0, max_value=10, step=1)
IneffectiveDisasterPreparedness = st.number_input("Ineffective Disaster Preparedness", min_value=0, max_value=10, step=1)
DrainageSystems = st.number_input("Drainage Systems", min_value=0, max_value=10, step=1)
CoastalVulnerability = st.number_input("Coastal Vulnerability", min_value=0, max_value=10, step=1)
Landslides = st.number_input("Landslides", min_value=0, max_value=10, step=1)
Watersheds = st.number_input("Watersheds", min_value=0, max_value=10, step=1)
DeterioratingInfrastructure = st.number_input("Deteriorating Infrastructure", min_value=0, max_value=10, step=1)
PopulationScore = st.number_input("Population Score", min_value=0, max_value=10, step=1)
WetlandLoss = st.number_input("Wetland Loss", min_value=0, max_value=10, step=1)
InadequatePlanning = st.number_input("Inadequate Planning", min_value=0, max_value=10, step=1)
PoliticalFactors = st.number_input("Political Factors", min_value=0, max_value=10, step=1)

# Create a button to make predictions
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
    st.success(f"The prediction is: {prediction[0]}")
