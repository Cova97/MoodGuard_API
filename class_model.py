import openai
import os
from dotenv import load_dotenv

# Cargar las variables de entorno
load_dotenv()

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
        self.emergency_numbers = {
            "SAPTEL": "55 5259 8121",
            "LOCATEL": "555 658 1111"
        }

    def add_user_message(self, message):
        self.messages.append({"role": "user", "content": message})

    def get_response(self):
        try:
            # Verificar palabras clave en el mensaje del usuario antes de solicitar a OpenAI
            user_message = self.messages[-1]["content"]
            if self.is_emergency_detected(user_message):
                return self._generate_emergency_message()

            # Obtener respuesta de OpenAI
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=self.messages,
                temperature=0.7,
                top_p=1.0
            )
            message_content = response['choices'][0]['message']['content']
            self.messages.append({"role": "system", "content": message_content})

            # Verificar palabras clave en la respuesta generada
            if self.is_emergency_detected(message_content):
                return f"{message_content}\n\n{self._generate_emergency_message()}"

            return message_content
        except Exception as e:
            return "Lo siento, ocurrió un error al procesar tu mensaje. Por favor, inténtalo nuevamente."

    def is_emergency_detected(self, message_content):
        # Lista de palabras clave que indican una emergencia
        emergency_keywords = ["suicidio", "matarme", "sin esperanza", "crisis", "muy grave", "sin salida"]

        # Verificar si alguna palabra clave está en el mensaje
        detected_keywords = [keyword for keyword in emergency_keywords if keyword in message_content.lower()]
        print("Palabras clave detectadas:", detected_keywords)  # Depuración
        return any(detected_keywords)

    def _generate_emergency_message(self):
        return (
            "Detecté que podrías estar enfrentando una situación difícil. No estás solo. "
            "Te recomiendo que te comuniques a uno de los siguientes números de emergencia:\n\n"
            f"Consejería SAPTEL: {self.emergency_numbers['SAPTEL']} (Disponible 24/7)\n"
            f"Línea de Ayuda LOCATEL: {self.emergency_numbers['LOCATEL']} (Disponible 24 horas al día)"
        )



    
