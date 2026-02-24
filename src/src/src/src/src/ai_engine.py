from openai import OpenAI

def generate_insight(technical, fundamentals, qualitative):
    client = OpenAI()

    prompt = f"""
    Technical Analysis:
    {technical}

    Fundamental Analysis:
    {fundamentals}

    Qualitative Context:
    {qualitative}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a senior financial analyst."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content
