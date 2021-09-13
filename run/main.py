from flask import Flask
import os
import random

app = Flask(__name__)  # Create a Flask object.
PORT = os.environ.get("PORT")  # Get PORT setting from environment.

# The app.route decorator routes any GET requests sent to the root path
# to this function, which responds with a "Hello world!" HTML document.
# If something is specified as the URL path (after the '/'), say_hello()
# responds with "Hello X", where X is the string at the end of the URL.
@app.route("/", methods=["GET"])
@app.route("/<name>", methods=["GET"])
def say_hello(name="world"):
    html = f"<h1>Hello {name}!</h1>"
    return html


# This code ensures that your Flask app is started and listens for
# incoming connections on the local interface and port 8080.
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)