from flask import Flask, render_template, request
from deep_translator import GoogleTranslator

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    translated_text = ""
    if request.method == 'POST':
        original_text = request.form.get('original_text', '')
        source_lang = request.form.get('source_language', 'auto')
        target_lang = request.form.get('language', 'en')
        
        if original_text.strip() == '':
            translated_text = "Please enter text to translate."
        else:
            try:
                translated_text = GoogleTranslator(source=source_lang, target=target_lang).translate(original_text)
            except Exception as e:
                translated_text = f"Error: {e}"

    return render_template('index.html', translated_text=translated_text)

if __name__ == '__main__':
    app.run(debug=True)
