from flask import Flask
import os
from dotenv import load_dotenv

load_dotenv()
app=Flask(__name__)

@app.route("/")
def home():
    environment = os.getenv("ENVIRONMENT", "unknown")
    db_url=os.getenv("DATABASE_URL")
    return f"<H2>Hello Sayem from the {environment} environment!</h2><p> DB URL: {db_url}</p>"

if __name__ =="__main__":
    app.run(debug=True)