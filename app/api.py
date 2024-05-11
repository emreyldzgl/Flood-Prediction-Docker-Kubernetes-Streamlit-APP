import uvicorn
from fastapi import FastAPI
import numpy as np
import joblib
from pydantic.main import BaseModel

app = FastAPI(title="Flood ML App")

@app.get('/')
def home():
    return "API is working as expected."

class MyData(BaseModel):
         MonsoonIntensity: int
         TopographyDrainage: int
         RiverManagement: int
         Deforestation: int
         Urbanization: int
         ClimateChange: int
         DamsQuality: int
         Siltation: int
         AgriculturalPractices: int
         Encroachments: int
         IneffectiveDisasterPreparedness: int
         DrainageSystems: int
         CoastalVulnerability: int
         Landslides: int
         Watersheds: int
         DeterioratingInfrastructure: int
         PopulationScore: int
         WetlandLoss: int
         InadequatePlanning: int
         PoliticalFactors: int

@app.post('/predict')
def predict(data: MyData):
    my_model = joblib.load('model.pkl')
    X = np.array([
        data.MonsoonIntensity,
        data.TopographyDrainage,
        data.RiverManagement,
        data.Deforestation,
        data.Urbanization,
        data.ClimateChange,
        data.DamsQuality,
        data.Siltation,
        data.AgriculturalPractices,
        data.Encroachments,
        data.IneffectiveDisasterPreparedness,
        data.DrainageSystems,
        data.CoastalVulnerability,
        data.Landslides,
        data.Watersheds,
        data.DeterioratingInfrastructure,
        data.PopulationScore,
        data.WetlandLoss,
        data.InadequatePlanning,
        data.PoliticalFactors
    ]).reshape(1, -1)
    return str(my_model.predict(X))

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
