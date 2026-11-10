from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Augestel Webhook Server Aktif"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json(silent=True)
    print("Webhook diterima:", data)
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
