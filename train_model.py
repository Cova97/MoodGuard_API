import openai
import os
from dotenv import load_dotenv

# Cargar las variables de entorno
load_dotenv()

# Configurar la API de OpenAI
API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = API_KEY

################################### openai gpt-4o ###################################
# Realizar la llamada a la API de ChatCompletion con un modelo más moderno
response = openai.ChatCompletion.create(
    model="gpt-4o",  # Usa el modelo más moderno
    messages=[
        {"role": "system", "content": "Eres un asistente que ayuda a detectar síntomas de depresión. Si te preguntan otras cosas fuera de tema, responde con 'No entiendo'."},
        {"role": "user", "content": "Me siento cansado y sin motivación."}
    ],
    
    temperature=0.7, # Controla la creatividad del modelo
    top_p=1.0 # Controla la diversidad del modelo
)

# Extraer y mostrar la respuesta del modelo
print(response['choices'][0]['message']['content'].strip())
