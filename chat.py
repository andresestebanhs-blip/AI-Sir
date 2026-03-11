import random
import json
import torch
from model import NeuralNet
from nltk_utils import bag_of_words, tokenize
from web_search import search_web

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('intents.json', 'r', encoding='utf-8') as f:
    intents = json.load(f)

FILE = "data.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data["all_words"]
tags = data["tags"]
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

bot_name = "AI-Sir"
print("Bienvenido, señor. Soy AI-Sir. Estoy a su disposición. Escriba 'salir' para retirarme.")

while True:
    sentence = input("Usted: ")
    if sentence == "salir":
        print(f"{bot_name}: Como desee, señor. Que tenga un excelente día.")
        break

    sentence = tokenize(sentence)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    
    # Threshold for confidence
    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent['tag']:
                print(f"{bot_name}: {random.choice(intent['responses'])}")
    else:
        print(f"{bot_name}: Mis disculpas, señor. No tengo esa información en mi memoria. Permítame investigar en la red...")
        # Join words back to sentence for search
        query = " ".join(sentence)
        result = search_web(query)
        if result:
            print(f"{bot_name}: Esto es lo que he encontrado, señor:\n{result}")
        else:
            print(f"{bot_name}: Lo lamento profundamente, pero no he podido conectar con los servicios de información externos.")
