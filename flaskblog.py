from flask import Flask, render_template
app = Flask(__name__, template_folder='bueno', static_folder="bueno")


@app.route('/')
@app.route('/home')
@app.route('/bueno/index.html')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return "About Page!"


if __name__ == "__main__":
    app.run(debug=True)
