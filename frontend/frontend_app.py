from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return render_template("home.html")


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', hide_buttons=True)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)