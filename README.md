# 🚗 AI Used Car Price Predictor API

An AI-powered FastAPI application that predicts the estimated resale price range of used cars in India using Large Language Models (LLMs) via LangChain and OpenAI.

---

# 📌 Features

- Predicts used car price range in lakh rupees
- Uses OpenAI LLM through LangChain
- REST API built with FastAPI
- Structured request validation using Pydantic
- Environment variable support using dotenv
- Easy to extend for ML models or database integration

---

# 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Backend language |
| FastAPI | REST API framework |
| LangChain | LLM orchestration |
| OpenAI | AI model |
| Pydantic | Data validation |
| dotenv | Environment variable management |

---

# 📂 Project Structure

```bash
project/
│
├── main.py
├── .env
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone <your-repo-url>
cd <project-folder>
```

---

## 2️⃣ Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux/Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 📦 Required Packages

Create a `requirements.txt` file with:

```txt
fastapi
uvicorn
langchain
langchain-openai
python-dotenv
pydantic
```

Install:

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file:

```env
OPENAI_API_KEY=your_openai_api_key
```

---

# ▶️ Run Application

```bash
uvicorn main:app --reload
```

Server will start at:

```txt
http://127.0.0.1:8000
```

---

# 📘 Swagger API Documentation

FastAPI automatically generates API docs.

Open:

```txt
http://127.0.0.1:8000/docs
```

---

# 🚘 API Endpoint

## POST `/predict-price/`

Predict estimated used car price.

### Request Body

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

# ✅ Sample Response

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
  "price_estimate": "Estimated price range: 7–8 lakh\nReason: Honda City has strong resale value, moderate mileage, and single ownership which increases buyer confidence."
}
```

---

# 🧠 How It Works

1. User sends car details through API
2. FastAPI validates request using Pydantic
3. LangChain formats prompt dynamically
4. OpenAI model generates estimated price range
5. API returns structured response

---

# 🔄 LangChain Workflow

```text
User Input
    ↓
PromptTemplate
    ↓
LangChain Chain
    ↓
OpenAI LLM
    ↓
Price Estimation Response
```

---

# 🚀 Future Improvements

- Add real ML regression model
- Store prediction history in database
- Add authentication
- Deploy on AWS/GCP/Azure
- Add frontend UI
- Dockerize application
- Add car image analysis

---

# 🐳 Docker Support (Future)

Example Docker deployment can be added for production-ready hosting.

---

# ☁️ Deployment Options

You can deploy this project on:

- AWS EC2
- Render
- Railway
- Azure App Service
- Google Cloud Run
- Docker Containers

---

# 👨‍💻 Author

Kaustubh Tole

AI/ML Enthusiast | AI for Engineering Applications

---

# 📜 License

This project is for educational and portfolio purposes.