import os
import pandas as pd
from dotenv import load_dotenv

load_dotenv()
MODEL = os.getenv("MODEL", "gemini")

if MODEL == "gpt":
    from llm_clients.gpt_client import GPTClient as ChosenClient
elif MODEL == "gemini":
    from llm_clients.gemini_client import GeminiClient as ChosenClient
else:
    raise ValueError(f"Unsupported MODEL: {MODEL}")

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


def main():
    client = ChosenClient()
    df = load_portfolio("holdings.csv")
    summary = create_summary(df)
    print("📊 Portfolio Summary:")
    print(summary)
    prompt = f"""
    You are a financial advisor AI. Analyze this stock portfolio summary and provide:
    1. 3 observations about sector diversification and risks.
    2. 2 suggestions to improve the portfolio.

    Portfolio Summary:
    {summary}
    """

    answer = client.ask(prompt)
    print("\n📈 AI Portfolio Advisor Says:\n")
    print(answer)
if __name__ == "__main__":
    main()

