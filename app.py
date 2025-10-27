from flask import Flask
import os

app=Flask(__name__)

@app.route("/")
def home():
    environment = os.getenv("ENVIRONMENT", "unknown")
    return f"Hello Sayem from the {environment} environment!"

if __name__ =="__main__":
    app.run(debug=True)