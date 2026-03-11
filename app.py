from flask import Flask, render_template, request, jsonify
import torch
import random
import json
from model import NeuralNet
from utils import bag_of_words, tokenize

app = Flask(__name__)

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Cargar intenciones
try:
    with open('intents.json', 'r', encoding='utf-8') as f:
        intents = json.load(f)
except FileNotFoundError:
    print("ERROR FATAL: No se encontró 'intents.json'.")
    exit()

# Cargar modelo entrenado
FILE = "data.pth"
try:
    data = torch.load(FILE)
except FileNotFoundError:
    print("ERROR: No se encontró 'data.pth'. Ejecuta 'python train.py' primero.")
    exit()

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data["all_words"]
tags = data["tags"]
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

def get_response(msg):
    sentence = tokenize(msg)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)
    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    
    # UMBRAL DE CONFIANZA REDUCIDO: 60%
    if prob.item() > 0.60:
        for intent in intents['intents']:
            if tag == intent['tag']:
                return random.choice(intent['responses'])
    else:
        # Fallback inteligente: si la probabilidad es baja pero no nula,
        # podríamos intentar sugerir algo, pero por ahora mantenemos el mensaje de error.
        return f"Mis disculpas (Confianza: {prob.item():.2f}), mi entrenamiento no cubre ese concepto específico. Prueba simplificando la frase."

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    text = request.get_json().get("message")
    response = get_response(text)
    message = {"answer": response}
    return jsonify(message)

if __name__ == "__main__":
    app.run(debug=True)

# Deploy for Render
