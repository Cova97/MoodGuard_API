import openai
import os
# from dotenv import load_dotenv

# Cargar las variables de entorno
# load_dotenv()

# Configurar la API de OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

class MoodGuardian:
    def __init__(self):
        # Mensaje inicial del asistente
        self.messages = [
            {
                "role": "system", 
                "content": (
                    "Eres un asistente que ayuda a detectar síntomas de depresión, felicidad y otras emociones. "
                    "Si detectas emociones negativas, ofreces ayuda. Si detectas buenas emociones, felicitas al usuario. "
                    "Si te preguntan algo fuera de este tema, responde con 'No entiendo'."
                )
            }
        ]

    def add_user_message(self, message):
        self.messages.append({"role": "user", "content": message})

    def get_response(self):
        # Obtener la respuesta de OpenAI
        response = openai.ChatCompletion.create(
            model="gpt-4o",  # Modelo actualizado
            messages=self.messages,
            temperature=0.7,
            top_p=1.0
        )
        # Agregar la respuesta del asistente al historial de mensajes
        message_content = response['choices'][0]['message']['content']
        self.messages.append({"role": "system", "content": message_content})
        return message_content
