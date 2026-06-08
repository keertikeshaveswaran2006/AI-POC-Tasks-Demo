from flask import Flask, jsonify, render_template
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/run/script1')
def run_script1():
    result = subprocess.run(
        ['python', 'MultipleChoiceQuestions.py'],
        capture_output=True,
        text=True
    )
    return jsonify({"output": result.stdout})

@app.route('/run/script2')
def run_script2():
    result = subprocess.run(
        ['python', 'CharacterRecognition.py'],
        capture_output=True,
        text=True
    )
    return jsonify({"output": result.stdout})

@app.route('/run/script3')
def run_script3():
    result = subprocess.run(
        ['python', 'Translate.py'],
        capture_output=True,
        text=True
    )
    return jsonify({"output": result.stdout})

if __name__ == '__main__':
    app.run(debug=True)
