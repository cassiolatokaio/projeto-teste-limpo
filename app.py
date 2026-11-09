import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/ping')
def ping():
    # PERIGO: O usuário pode injetar comandos aqui!
    ip = request.args.get('ip')
    return os.system("ping -c 1 " + ip)
