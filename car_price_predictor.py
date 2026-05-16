from fastapi import FastAPI
from langchain_openai import OpenAI
from langchain_core.prompts import PromptTemplate 
from pydantic import BaseModel 
from dotenv import load_dotenv
import os 

load_dotenv()

app = FastAPI(title="Car Price Predictor API", description="Predict car prices using OpenAI")

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

llm = OpenAI(api_key=OPENAI_API_KEY)

price_prompt = PromptTemplate.from_template("""
You are an expert used-car dealer in India.
Given the details below, estimate a fair price range in lakh rupees and explain in 3–4 lines.

Car model: {model}
Year: {year}
Kilometers driven: {km_driven}
Fuel type: {fuel_type}
Transmission: {transmission}
City: {city}
Number of owners: {owners}
Overall condition: {condition}

Return answer in this format:
Estimated price range: X–Y lakh
Reason: <short reason>
""")

price_chain = price_prompt | llm



class UsedCarRequest(BaseModel):
    model: str
    year: int
    km_driven: int
    fuel_type: str      # e.g. "Petrol", "Diesel", "CNG"
    transmission: str   # e.g. "Manual", "Automatic"
    city: str
    owners: int         # e.g. 1, 2
    condition: str      # e.g. "excellent", "good", "average"


@app.post("/predict-price/")
async def predict_price(request: UsedCarRequest):
    # request.dict() turns Pydantic model into normal dict
    inputs = request.dict()

    result = price_chain.invoke(inputs)

    return {
        "car_details": inputs,
        "price_estimate": result
    }
