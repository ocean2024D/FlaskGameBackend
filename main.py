from flask import Flask, jsonify
from flask_cors import CORS
CORS(app)

app = Flask(__name__)

@app.route('/api/message', methods=['GET'])
def get_message():
    return jsonify({'message': 'Merhaba, React ve Flask ile bağlantı başarılı!'})

if __name__ == '__main__':
    app.run(debug=True)
