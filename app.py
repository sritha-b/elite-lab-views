from flask import Flask, render_template
app = Flask(__name__)

app.config['ENV'] = 'development'

@app.route('/')
def index():
  return render_template('index.html', title="My Website")

@app.route('/exercise/')
def exercise():
  return render_template('exercise.html', title="Lab Exercise")
