import pandas as pd
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
OpenAI.api_key = os.getenv("OPENAI_API_KEY")

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

def query_gpt(summary):
    client = OpenAI()
    prompt = f"""
    You are a financial advisor AI. Analyze this stock portfolio summary and provide:
    1. 3 observations about sector diversification and risks.
    2. 2 suggestions to improve the portfolio.

    Portfolio Summary:
    {summary}
    """

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content

def main():
    df = load_portfolio("holdings.csv")
    summary = create_summary(df)
    print("📊 Portfolio Summary:")
    print(summary)

    print("\n🤖 GPT Analysis:")
    print(query_gpt(summary))

if __name__ == "__main__":
    main()