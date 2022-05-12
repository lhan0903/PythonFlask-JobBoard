from flask import Flask, render_template

# create an instance of Flask class
app = Flask(__name__)

@app.route('/')
@app.route('/jobs')
def jobs():
    return render_template('index.html')