from openai import OpenAI

client = OpenAI(
    api_key='API_KEY'
    )

def get_car_ai_bio(model, brand, year):
    try:
        message = f"""
        Encontre informações sobre o {brand} {model} ano {year}.
        Organize as informações de forma clara e concisa.
        """
        completion = client.chat.completions.create(
            model="gpt-4",
            max_tokens=1000,
            messages=[
                {
                    "role": "system",
                    "content": "Você é um assistente especializado em informações automotivas."
                },
                {
                    "role": "user",
                    "content": message
                }
            ]
        )
        return completion.choices[0].message.content
    except Exception as e:
        return "Carro em excelente condição, único dono, venha conferir!"