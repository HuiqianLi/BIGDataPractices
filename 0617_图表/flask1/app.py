from flask import Flask, render_template
import static
app = Flask(__name__)


@app.route('/')
def mainhtml():
    return render_template("index.html")


if __name__ == '__main__':
    app.run()
