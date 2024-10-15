from flask import Flask, request, jsonify
from flask_cors import CORS
from class_model import MoodGuardian

app = Flask(__name__)
CORS(app)

# Crear una instancia de MoodGuardian
mood_guardian = MoodGuardian()

@app.route("/chat", methods=["POST"])
def chat():
    try:
        # Verificar que el mensaje esté presente en el cuerpo de la solicitud
        data = request.get_json()
        if data is None or "message" not in data:
            return jsonify({"error": "Mensaje no encontrado"}), 400
        
        user_message = data["message"]
        mood_guardian.add_user_message(user_message)
        response = mood_guardian.get_response()
        return jsonify({"message": response}), 200
    
    except Exception as e:
        # Manejo de excepciones generales
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
