from openai import OpenAI

#client = OpenAI(api_key='API_KEY')
client = OpenAI(base_url="http://127.0.0.1:1234/v1", api_key="lm-studio")
MODEL = "llama-3.2-1b-instruct"  # Make sure this model exists in LM Studio

def get_car_ai_bio(model, brand, year):
    try:
        message = f"""
        Encontre informações sobre o {brand} {model} ano {year}.
        Organize as informações de forma clara e concisa.
        """
        completion = client.chat.completions.create(
            model=MODEL,
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
        return "Não foi possível encontrar informações para este veículo." # Mensagem de erro mais informativa