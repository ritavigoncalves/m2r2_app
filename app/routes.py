from app import app
from flask import render_template

@app.route("/")
@app.route("/index")
@app.route("/api",methods=['POST'])
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(port=5000, debug=True)