from flask import Flask, jsonify
from flask_cors import CORS
import random 

app = Flask(__name__)
CORS(app)
@app.route('/api/message', methods=['GET'])
def get_message():
    return jsonify({'message': 'Merhaba, React ve Flask ile bağlantı başarılı!'})


@app.route('/api/list')
def list():
    numbers = [1, 2, 3, 4, 5]
    return jsonify(numbers)
@app.route("/api/game")
def game():
    words = ["vélo: 🚴",
"maison: 🏚️",
"voiture: 🚗",
"banane: 🍌",
"chaise: 🪑",
"chat: 😻",
"zèbre: 🦓",
"ours polaire: 🐻‍❄️",
"chien: 🦮🐕🐩🐶",
"mouton: 🐑",
"cheval: 🐎",
"chocolat: 🍫",
"frite: 🍟",
"spaghetti: 🍝",
"fantôme: 👻",
"tête de mort: ☠️",
"diable: 😈",
"extraterrestre: 👽",
"arbre: 🌳",
"fleur: 🌸",
"soleil: 🌞",
"lune: 🌙",
"étoile: ⭐",
"nuage: ☁️",
"pluie: 🌧️",
"bateau: 🚤",
"train: 🚆",
"moto: 🏍️",
"bus: 🚍",
"taxi: 🚖",
"métro: 🚇",
"ordinateur: 💻",
"téléphone: 📱",
"télévision: 📺",
"radio: 📻",
"appareil photo: 📷",
"caméra: 🎥",
"livre: 📚",
"carnet: 📒",
"stylo: 🖊️",
"pinceau: 🖌️",
"guitare: 🎸",
"piano: 🎹",
"tambour: 🥁",
"trompette: 🎺",
"violon: 🎻",
"cloche: 🔔",
"médaille: 🏅",
"trophée: 🏆",
"ballon de football: ⚽",
"basket-ball: 🏀",
"tennis: 🎾",
"baseball: ⚾",
"golf: ⛳",
"ping-pong: 🏓",
"rugby: 🏉",
"yoga: 🧘",
"musculation: 🏋️‍♀️",
"danse: 💃",
"course: 🏃‍♀️",
"natation: 🏊‍♀️",
"vélo: 🚴‍♀️"
]
    options = random.sample(words, 4)       
    correct = random.choice(options)        
    return jsonify({
        "randomWord": correct,
        "shuffledWords": options
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
