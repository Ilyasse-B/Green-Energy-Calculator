import os
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict

app = FastAPI(title="EV Charging Environmental Impact Calculator")

class EnergyInput(BaseModel):
    energy_kwh: float  # Energy consumed in kilowatt-hours

@app.post("/calculate")
def calculate_environmental_impact(data: EnergyInput) -> Dict[str, float]:
    energy_kwh = data.energy_kwh

    # Constants based on UK data
    MILES_PER_KWH = 3.5  # Average miles per kWh for EVs
    CO2_PER_MILE_G = 211.2  # Average CO2 emissions per mile for ICE vehicles in grams
    NO2_PER_MILE_G = 0.146  # Average NO2 emissions per mile for ICE vehicles in grams
    METHANE_PER_MILE_G = 0.02  # Estimated CH4 emissions per mile for ICE vehicles in grams
    TREE_CO2_ABSORPTION_KG_PER_YEAR = 22  # Average CO2 absorption per tree per year in kg
    ICE_CAR_MILES_PER_MONTH = 1000  # Average monthly mileage for ICE vehicles

    # Calculations
    ev_miles = energy_kwh * MILES_PER_KWH
    co2_saved_kg = (ev_miles * CO2_PER_MILE_G) / 1000  # Convert grams to kilograms
    no2_saved_kg = (ev_miles * NO2_PER_MILE_G) / 1000
    methane_saved_kg = (ev_miles * METHANE_PER_MILE_G) / 1000
    total_ghg_saved_kg = co2_saved_kg + no2_saved_kg + methane_saved_kg
    trees_equivalent = co2_saved_kg / TREE_CO2_ABSORPTION_KG_PER_YEAR
    ice_cars_off_road = ev_miles / ICE_CAR_MILES_PER_MONTH

    return {
        "ev_miles_charged": round(ev_miles, 2),
        "co2_saved_kg": round(co2_saved_kg, 2),
        "no2_saved_kg": round(no2_saved_kg, 2),
        "methane_saved_kg": round(methane_saved_kg, 2),
        "total_ghg_saved_kg": round(total_ghg_saved_kg, 2),
        "trees_equivalent": round(trees_equivalent, 2),
        "ice_cars_off_road": round(ice_cars_off_road, 2),
        "ice_miles_equivalent": round(ev_miles, 2)  # Same as ev_miles_charged
    }

# Required for Render deployment
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))  # Render provides this environment variable
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=False)