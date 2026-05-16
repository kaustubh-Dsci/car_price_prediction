from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI(
    title="Car Price Predictor API",
    description="Predict car prices using OpenAI"
)

# Allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(
    api_key=OPENAI_API_KEY,
    model="gpt-4o-mini"
)

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
    fuel_type: str
    transmission: str
    city: str
    owners: int
    condition: str


@app.post("/predict-price/")
async def predict_price(request: UsedCarRequest):

    inputs = request.dict()

    result = price_chain.invoke(inputs)

    return {
        "car_details": inputs,
        "price_estimate": result.content
    }