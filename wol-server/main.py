from flask import Flask, request
from wakeonlan import send_magic_packet
import os

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return "Servidor WOL funcionando!", 200

@app.route("/wol", methods=["POST"])
def wake_pc():
    mac = "04:7C:16:D0:B5:F1"  # Formato correto
    send_magic_packet(mac)
    return "Pacote mágico enviado!", 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
