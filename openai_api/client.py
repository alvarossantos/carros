# No seu arquivo da função
import google.generativeai as genai
from django.conf import settings

# Configura a API do Gemini com a chave do settings
genai.configure(api_key=settings.GEMINI_API_KEY)

def get_car_ai_bio(model, brand, year):
    try:
        # Prepara o modelo do Gemini
        generation_config = {
            "candidate_count": 1,
            "temperature": 0.7,
        }
        gemini_model = genai.GenerativeModel(
            model_name="gemini-2.0-flash", # ou outro modelo do Gemini
            generation_config=generation_config
        )

        # Monta a mensagem para a IA
        message = f"""
        Fale sobre o carro {brand} {model} ano {year}.
        No máximo 100 palavras.
        """

        # Gera o conteúdo
        response = gemini_model.generate_content(message)
        return response.text

    except Exception as e:
        print(f"Ocorreu um erro na API do Gemini: {e}")
        return "Carro em excelente condição, único dono, venha conferir!"