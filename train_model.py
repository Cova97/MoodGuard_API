import openai
import os
import json
import time
from dotenv import load_dotenv

# Cargar las variables de entorno
load_dotenv()

# Configurar la API de OpenAI
API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = API_KEY

# Funcion para subor los datos de entrenamiento
def upload_training_data(json_file):
    with open(json_file, 'rb') as f:
        response = openai.File.create(file=f, purpose='fine-tune')
    return response['id']

# Funcion para iniciar el fine-tuning del modelo
def fine_tune_model(training_file_id, base_model="gpt-3.5-turbo-1106"):
    response = openai.FineTune.create(
        training_file=training_file_id,
        model = base_model,
    )
    return response['id']
    
# Función para monitorear el progreso del fine-tuning
def monitor_fine_tuning(fine_tune_id):
    while True:
        status_response = openai.FineTune.retrieve(fine_tune_id)
        status = status_response['status']
        print(f"Estado actual del entrenamiento: {status}")
        
        # Termina si el fine-tuning ha terminado o ha fallado
        if status in ["succeeded", "failed"]:
            break
        time.sleep(60)  # Espera 1 minuto antes de verificar nuevamente
    return status_response['fine_tuned_model']

# Función para usar el modelo entrenado
def use_fine_tuned_model(model_name, prompt):
    response = openai.ChatCompletion.create(
        model=model_name,
        messages=[
            {"role": "system", "content": "Eres un asistente que detecta síntomas de depresión."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=150
    )
    return response['choices'][0]['message']['content']

# Ejecución del proceso completo
if __name__ == "__main__":
    # Archivo combinado con ejemplos de depresión y no-depresión
    combined_data_file = 'json/data_set.json'

    # Subir el archivo combinado de datos de entrenamiento
    training_file_id = upload_training_data(combined_data_file)
    print(f"ID del archivo de entrenamiento: {training_file_id}")

    # Iniciar el fine-tuning del modelo
    fine_tune_id = fine_tune_model(training_file_id)
    print(f"ID del fine-tuning iniciado: {fine_tune_id}")

    # Monitorear el progreso del entrenamiento
    fine_tuned_model = monitor_fine_tuning(fine_tune_id)
    print(f"Modelo ajustado: {fine_tuned_model}")

    # Usar el modelo ajustado con un ejemplo de input
    test_prompt = "Me siento cansado y sin energía todos los días."
    result = use_fine_tuned_model(fine_tuned_model, test_prompt)
    print(f"Resultado: {result}")

# # Realizar la llamada a la API de ChatCompletion con un modelo más moderno
# response = openai.ChatCompletion.create(
#     model="gpt-4o",  # Usa el modelo más moderno
#     messages=[
#         {"role": "system", "content": "Eres un asistente que ayuda a detectar síntomas de depresión. Si te preguntan otras cosas fuera de tema, responde con 'No entiendo'."},
#         {"role": "user", "content": "Me siento cansado y sin motivación."}
#     ],
    
#     temperature=0.7, # Controla la creatividad del modelo
#     top_p=1.0 # Controla la diversidad del modelo
# )

# # Extraer y mostrar la respuesta del modelo
# print(response['choices'][0]['message']['content'].strip())
