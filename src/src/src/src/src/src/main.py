from market_data import get_market_data
from technical_analysis import calculate_technical_indicators
from fundamentals import get_fundamentals
from qualitative import get_qualitative_context
from ai_engine import generate_insight

def run():
    market_data = get_market_data()
    technicals = calculate_technical_indicators(market_data)
    fundamentals = get_fundamentals()
    qualitative = get_qualitative_context()

    insight = generate_insight(technicals, fundamentals, qualitative)
    print(insight)

if __name__ == "__main__":
    run()
