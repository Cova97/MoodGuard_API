# **MoodGuard: IA para la Detección de Síntomas de Depresión**

MoodGuard es una herramienta de inteligencia artificial diseñada para ayudar a detectar síntomas de depresión en textos escritos. Utiliza el modelo de lenguaje GPT-4 ajustado para identificar posibles indicios de depresión en el lenguaje cotidiano, proporcionando una indicación rápida de si los síntomas están presentes o no.

Este proyecto está desarrollado en Python y utiliza la API de OpenAI para realizar el análisis del texto. Está diseñado para ser implementado con Flask como backend y desplegado en Render usando Gunicorn como servidor WSGI.

## **Características**
- Detección de síntomas de depresión basados en entradas de texto.
- Respuestas claras: "Síntomas de depresión detectados" o "No hay síntomas de depresión".
- Si el texto no es relevante al tema, responderá: "No estoy diseñado para responder esto."
- Desplegable fácilmente en plataformas como **Render**.

## **Tecnologías**
- **Lenguaje de programación**: Python
- **Librerías principales**:
  - `openai`: Para realizar las llamadas a la API de OpenAI.
  - `requests`: Para manejar las solicitudes HTTP.
  - `flask`: Framework web ligero para el desarrollo del backend.
  - `gunicorn`: Servidor WSGI para producción.
  
## **Requisitos del sistema**
- Python 3.8 o superior.
- Cuenta de OpenAI para obtener una API Key.

## **Instalación**

### **1. Clonar el repositorio**
```bash
git clone https://github.com/tu_usuario/moodguard.git
cd moodguard
```

### **2. Crear y activar un entorno virtual**
Es recomendable trabajar en un entorno virtual para mantener las dependencias aisladas.

En Linux/Mac:
```bash
python3 -m venv venv
source venv/bin/activate
```

En Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

### **3. Instalar las dependencias**
Las dependencias están listadas en el archivo `requirements.txt`. Para instalar todas las dependencias necesarias, ejecuta el siguiente comando:

```bash
pip install -r requirements.txt
```

### **4. Configurar la API Key de OpenAI**
1. Crea una cuenta en [OpenAI](https://beta.openai.com/signup/).
2. Dirígete al panel de control de la cuenta de OpenAI, selecciona **API Key**, y genera una nueva clave de API.
3. Crea un archivo `.env` en el directorio raíz del proyecto con el siguiente contenido:
   ```bash
   OPENAI_API_KEY=tu_api_key_aqui
   ```

### **5. Ejecutar la aplicación localmente**
Para ejecutar la aplicación de manera local, usa el comando de Flask:

```bash
flask run
```

Esto levantará la aplicación en `http://127.0.0.1:5000/`.

### **6. Desplegar en producción con Gunicorn**
Cuando estés listo para desplegar la aplicación, por ejemplo, en **Render**, puedes usar Gunicorn. Asegúrate de haber configurado todo correctamente en Render y luego ejecuta:

```bash
gunicorn app:app
```

## **Despliegue en Render**
1. Crea una cuenta en [Render](https://render.com/).
2. Crea un nuevo servicio web y conecta tu repositorio de GitHub con Render.
3. Configura el servicio para que use **Gunicorn** como servidor WSGI con el comando:

   ```bash
   gunicorn app:app
   ```

4. Añade tu variable de entorno `OPENAI_API_KEY` en la configuración del servicio en Render.
5. Despliega la aplicación y Render se encargará del resto.

## **Uso**

Una vez que la aplicación esté ejecutándose, podrás enviarle textos y la IA los evaluará para determinar si existen síntomas de depresión o no. Ejemplos de uso:

```bash
POST /analizar

Body:
{
  "texto": "Me siento muy triste y sin energía."
}

Respuesta:
{
  "resultado": "El modelo indica que podrías tener síntomas de depresión."
}
```

Si envías algo no relacionado con el tema:

```bash
POST /analizar

Body:
{
  "texto": "¿Qué opinas sobre la inteligencia artificial?"
}

Respuesta:
{
  "resultado": "No estoy diseñado para responder esto."
}
```

## **Contribuciones**
Las contribuciones son bienvenidas. Si tienes sugerencias o encuentras algún error, por favor crea un **Issue** o envía un **Pull Request**.

## **Licencia**
Este proyecto está bajo la Licencia MIT. Para más información, consulta el archivo `LICENSE`.

---

## **Contacto**
Si tienes preguntas o sugerencias, no dudes en contactarnos en:

- Correo: acovamartinez@gmail.com
- GitHub: [Repositorio de MoodGuard](https://github.com/Cova97/DepreSacan_API)
