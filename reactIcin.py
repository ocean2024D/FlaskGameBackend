from flask import Flask, request, jsonify
from flask_cors import CORS  # React ile haberleşebilmesi için

app = Flask(__name__)
CORS(app)  # Tüm kaynaklar arası erişimi (CORS) açıyoruz

@app.route("/toplam", methods=["POST"])
def toplam():
    data = request.get_json()
    try:
        number1 = int(data.get("number1"))
        number2 = int(data.get("number2"))
        total = number1 + number2
        return jsonify({"total": total})
    except:
        return jsonify({"error": "Geçerli sayılar giriniz!"}), 400

if __name__ == "__main__":
    app.run(debug=True)
