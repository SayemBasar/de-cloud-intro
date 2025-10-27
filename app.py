from flask import Flask
import os
from dotenv import load_dotenv
from config import DevConfig, ProdConfig

# load_dotenv()
app=Flask(__name__)

environment = os.getenv("ENVIRONMENT", "development")

if environment=="production":
    load_dotenv(dotenv_path=".env.prod")
    # app.config.from_object(ProdConfig)
else:
    load_dotenv(dotenv_path=".env.dev")
    # app.config.from_object(DevConfig)


if environment=="production":
    app.config.from_object(ProdConfig)
else:
    app.config.from_object(DevConfig)


@app.route("/")
def home():
    return f"<H2>Hello Sayem from the {app.config["ENV"]} environment!</h2><p> DB URL: {app.config["DATABASE_URL"]}</p>"

if __name__ =="__main__":
    app.run(debug=app.config["DEBUG"])