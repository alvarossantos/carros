from openai import OpenAI

client = OpenAI(
    api_key='API_KEY'
)

def get_car_ai_bio(model, brand, year):
    try:
        message = '''Encontre informações sobre o veículo {brand} {model} {year}. Inclua detalhes como tipo de veículo, motor, consumo de combustível, e quaisquer prêmios ou reconhecimentos que tenha recebido.'''
        completion = client.chat.completions.create(
            model="gpt-4",
            max_tokens=1000,
            messages=[
                {
                    "role": "system",
                    "content": "Você é um assistente útil que busca informações sobre veículos."
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
