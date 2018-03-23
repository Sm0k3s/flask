from flask import Flask, render_template

app = Flask(__name__)

"""from app import views"""

app.config.from_object('config')


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/templates')
def books():
    return render_template("books.html")

if __name__ == "__main__":
	app.run()