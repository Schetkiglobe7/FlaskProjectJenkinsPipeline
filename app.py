from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_guys():
    return '<h1>Hello from Flask</h1>'

if __name__ == "__main__":
    app.run(debug=True)