from flask import Flask, render_template, request, jsonify
from chatbot import buscar_en_chromadb, enviar_a_deepseek  # ✅ Importar funciones necesarias

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def get_response():
    user_input = request.form["user_input"]
    
    # 1️⃣ Buscar contexto relevante en ChromaDB
    contexto = buscar_en_chromadb(user_input)

    # 2️⃣ Generar respuesta usando DeepSeek
    respuesta = enviar_a_deepseek(contexto, user_input)

    return jsonify({"response": respuesta})

if __name__ == "__main__":
    app.run(debug=True)
