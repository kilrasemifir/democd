from flask import Flask

app = Flask("demo-cd")

@app.get("/")
def hello():
    return "Hello world"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)