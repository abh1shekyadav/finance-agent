from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()
MODEL = os.getenv("MODEL", "gemini")

if MODEL == "gpt":
    from llm_clients.gpt_client import GPTClient as LLMClient
elif MODEL == "gemini":
    from llm_clients.gemini_client import GeminiClient as LLMClient
else:
    raise ValueError(f"Unsupported MODEL: {MODEL}")

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

llm_client = LLMClient()

class SummaryRequest(BaseModel):
    summary: str


def load_portfolio(file_path):
    df = pd.read_csv(file_path)
    return df

def create_summary(df):
    total_invested = (df['quantity'] * df['avg_price']).sum()
    total_value = (df['quantity'] * df['current_price']).sum()
    total_gain = total_value - total_invested
    sector_allocation = df.groupby('sector')['quantity'].sum().to_dict()

    summary = f"""
    Total invested: Rs.{total_invested:.2f}
    Current value: Rs.{total_value:.2f}
    Gain/Loss: Rs.{total_gain:.2f}
    Sector allocation: {sector_allocation}
    """
    return summary

@app.get("/ask-ai")
async def ask_ai():
     df = load_portfolio("holdings.csv")
     summary = create_summary(df)
     try:
        prompt = f"""
        You are a financial advisor AI. Analyze this stock portfolio summary and provide:
        1. 3 observations about sector diversification and risks.
        2. 2 suggestions to improve the portfolio.

        Portfolio Summary:
        {summary}
        """
        response = llm_client.ask(prompt)
        return {"response": response}
     except Exception as e:
        return {"error": str(e)}

@app.get("/")
def root():
    return {"message": "Finance Agent API is running"}

