from flask import Flask, render_template, request
from engine_logic import analyze_and_synthesize
import os

app = Flask(__name__)

# Ensure the audio output directory exists
if not os.path.exists('static/audio'):
    os.makedirs('static/audio')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text_input = request.form['text']
        if text_input:
            # Call our logic function
            audio_path, emotion, score = analyze_and_synthesize(text_input)

            # Render the page with the results
            return render_template('index.html', 
                                   text=text_input, 
                                   audio_path=audio_path, 
                                   emotion=emotion,
                                   polarity=round(score, 2))

    # Initial page load
    return render_template('index.html', text=None)

if __name__ == '__main__':
    app.run(debug=True)