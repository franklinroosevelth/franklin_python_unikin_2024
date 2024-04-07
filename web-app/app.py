from flask import Flask, request, render_template, jsonify
from chat import get_response
from settings import *

app = Flask(__name__)

@app.route("/")
def page_chat():
    return render_template('chat.html')

@app.route("/chat", methods=['POST'])
def chat():
    resp = ""
    if request.method == 'POST':
        message = request.form['message']
        resp = get_response(message)
        
    return jsonify({"reponse": resp}), 200, {'Content-Type': 'application/json; charset=utf-8'}

if __name__ == "__main__":
    app.run(debug = DEBUG, host =  HOST, port = PORT)