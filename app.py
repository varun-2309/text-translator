from flask import Flask, request, jsonify, render_template
from googletrans import Translator
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

translator = Translator()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    data = request.json
    translated = translator.translate(data['text'], src=data['source'], dest=data['target'])
    return jsonify({"translatedText": translated.text})

