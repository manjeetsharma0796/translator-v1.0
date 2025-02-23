from flask import Flask, request, jsonify
from deep_translator import GoogleTranslator
from flask_cors import CORS  # To allow frontend to communicate with backend

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend access

@app.route("/translate", methods=["POST"])
def translate_text():
    try:
        data = request.json  # Get JSON data from frontend
        text = data.get("text", "")
        language = data.get("language", "")

        if not text or not language:
            return jsonify({"error": "Missing text or language"}), 400

        # Translate text
        translated_text = GoogleTranslator(source="auto", target=language).translate(text)
        
        return jsonify({"translated_text": translated_text})
    
    except Exception as e:
        return jsonify({"error": "Translation failed", "details": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
