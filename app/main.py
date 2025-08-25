from flask import Flask
from app.crud_fichas import *

app = Flask(__name__)

@app.route("/")
def home():
    return "Servidor Rodando! CRUD de fichas pronto."

if __name__ == "__main__":
    app.run(debug=True)
