# ⚡ EV Charging Environmental Impact API

This FastAPI application calculates key environmental benefits based on energy (in kWh) consumed by electric vehicle (EV) chargers.

It returns:

- ✅ EV miles charged
- ✅ Greenhouse gas emissions saved (CO₂, NO₂, methane, total)
- ✅ Trees’ equivalent CO₂ absorption
- ✅ Internal combustion engine (ICE) car miles offset
- ✅ ICE cars taken off the road (monthly equivalent)

---

# This API has been deployed on Render at:
[Green Energy Calculator](https://green-energy-calculator.onrender.com)

It is slow to start because of free plan.

Use /calculate as the end point for the API.

The API is accessible from any HTTPS website through my CORS policy, so if you want to use this on your own web app, feel free

## 🚀 Getting Started

### 🧱 Prerequisites

- Python 3.8+
- `pip` installed

### 📦 Install Requirements

1. Clone the repository:
   ```bash
   [https://github.com/Ilyasse-B/Green-Energy-Calculator.git]
   cd Green-Energy-Calculator

2. Create a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install dependencies:
    ```bash
    pip install fastapi uvicorn pydantic

### ▶️ Running the API Locally

1. Start the API:
    ```bash
    uvicorn main:app --reload

2. Open your browser and go to:
    ```bash
    http://127.0.0.1:8000/docs
    
3. You’ll see the FastAPI Swagger UI. Scroll down to the POST /calculate endpoint.

4. Click "Try it out" and enter your energy usage like this:
    ```json
    {
        "energy_kwh": 1000
    }
    ```

5. Hit "Execute" to see your results!

### 📘 API Endpoint

#### POST /calculate

Request body:
```json
    {
    "energy_kwh": <float>  // Total energy consumed by EV chargers in kWh
    }
```
Sample Response:
```json
{
  "ev_miles_charged": 3500.0,
  "co2_saved_kg": 739.2,
  "no2_saved_kg": 0.51,
  "methane_saved_kg": 0.07,
  "total_ghg_saved_kg": 739.78,
  "trees_equivalent": 33.6,
  "ice_cars_off_road": 3.5,
  "ice_miles_equivalent": 3500.0
}
```
### 📊 Data Sources & References

All data is based on UK-specific environmental and transport statistics:

| Metric                        | Value         | Source                                                                                                                                                                                             |
| ----------------------------- | ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| EV Efficiency                 | 3.5 miles/kWh | [Energy Saving Trust – Fleet Decarbonisation Toolkit](https://fleetdecarbonisationtoolkit.energysavingtrust.org.uk/t/decarbonisation-strategy/emissions-calculated/car-van-ghg-kwh-calculations-2) |
| CO₂ per ICE mile              | 211.2 g       | [NimbleFins UK – Average CO₂ Emissions](https://www.nimblefins.co.uk/average-co2-emissions-car-uk)                                                                                                 |
| NO₂ per ICE mile              | 0.146 g       | [UK Gov – Transport and Environment Statistics 2023](https://www.gov.uk/government/statistics/transport-and-environment-statistics-2023)                                                           |
| Methane per ICE mile          | 0.02 g        | [UK Gov – Transport and Environment Statistics 2023](https://www.gov.uk/government/statistics/transport-and-environment-statistics-2023)                                                           |
| Tree CO₂ absorption/year      | 22 kg         | [UK Gov – Carbon offsetting guidance](https://www.gov.uk/government/publications/greenhouse-gas-reporting-conversion-factors-2023)                                                                 |
| ICE car average monthly miles | 1000 miles    | [UK Gov – Vehicle Usage](https://www.gov.uk/government/statistics/transport-and-environment-statistics-2023)                                                                                       |

### 🛠 Developer Notes
The API assumes constant average values across different types of EVs and ICE vehicles.

GHG emissions saved are calculated by comparing EV mileage to ICE equivalents.

Tree absorption is annual, so values represent equivalent annual tree effort.

### 📬 Questions?
Feel free to raise an issue or contact me.
