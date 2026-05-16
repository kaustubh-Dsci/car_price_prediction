# AI Car Price Predictor 🚗

An AI-powered used car price prediction web application built using:

* FastAPI
* LangChain
* OpenAI
* HTML/CSS/JavaScript

The application predicts a fair used-car price range in India based on car details such as model, year, fuel type, transmission, city, ownership, and overall condition.

---

# Features

* 🚗 Used car price prediction
* 🤖 AI-generated valuation using OpenAI
* ⚡ FastAPI backend
* 🌐 Simple frontend web interface
* 🔗 REST API integration
* 📄 Swagger API documentation
* 🎨 Responsive UI
* 🔒 Environment variable support using `.env`

---

# Tech Stack

## Backend

* Python
* FastAPI
* LangChain
* OpenAI API
* Uvicorn

## Frontend

* HTML
* CSS
* JavaScript

---

# Project Structure

```text
project/
│
├── car_price_predictor.py     # FastAPI backend
├── frontend/
│   ├── index.html             # Frontend UI
│   ├── style.css              # Styling
│   └── script.js              # API integration
│
├── .env                       # OpenAI API Key
├── requirements.txt
└── README.md
```

---

# Installation & Setup

## 1. Clone Repository

```bash
git clone <your-repository-url>
cd <project-folder>
```

---

# 2. Create Virtual Environment

## Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

## Linux / Mac

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

# 3. Install Dependencies

```bash
pip install fastapi uvicorn langchain langchain-openai python-dotenv
```

---

# 4. Create `.env` File

Create a file named:

```text
.env
```

Add your OpenAI API key:

```env
OPENAI_API_KEY=your_openai_api_key
```

---

# Backend Code

The backend is implemented using FastAPI and LangChain.

Main API endpoint:

```text
POST /predict-price/
```

---

# Run Backend Server

Start FastAPI server:

```bash
uvicorn car_price_predictor:app --reload
```

Server will run on:

```text
http://127.0.0.1:8000
```

---

# API Documentation

FastAPI automatically generates Swagger UI.

Open in browser:

```text
http://127.0.0.1:8000/docs
```

---

# Run Frontend

Open a new terminal.

Move into frontend directory:

```bash
cd frontend
```

Run local frontend server:

```bash
python -m http.server 5500
```

---

# Open Web Application

Open browser:

```text
http://127.0.0.1:5500
```

You will see:

* Car details form
* Predict Price button
* AI-generated price prediction

---

# Example API Request

```json
{
  "model": "Honda City",
  "year": 2018,
  "km_driven": 45000,
  "fuel_type": "Petrol",
  "transmission": "Manual",
  "city": "Pune",
  "owners": 1,
  "condition": "good"
}
```

---

# Example Response

```json
{
  "car_details": {
    "model": "Honda City",
    "year": 2018,
    "km_driven": 45000,
    "fuel_type": "Petrol",
    "transmission": "Manual",
    "city": "Pune",
    "owners": 1,
    "condition": "good"
  },
  "price_estimate": "Estimated price range: 7–8 lakh\nReason: Well-maintained Honda City with moderate mileage and strong resale value in Pune market."
}
```

---

# Application Architecture

```text
Frontend (HTML/CSS/JavaScript)
            ↓
Fetch API Request
            ↓
FastAPI Backend
            ↓
LangChain Prompt Chain
            ↓
OpenAI LLM
            ↓
AI Price Prediction
            ↓
Frontend Display
```

---

# Future Improvements

You can extend this project with:

* React frontend
* Real machine learning model
* Database integration
* User authentication
* Car image upload
* Dark mode UI
* Docker deployment
* Cloud deployment (AWS/Render/Railway)
* Car comparison feature
* RAG-based pricing system

---

# Learning Outcomes

This project demonstrates:

* FastAPI development
* REST API creation
* Frontend-backend integration
* LangChain usage
* OpenAI API integration
* Environment variable management
* AI application development
* Full-stack GenAI engineering

---

# License

MIT License

---

# Author

Kaustubh Tole

AI/ML | GenAI | Automation Engineering
