from flask import Flask
import os
import sys
import socket

app = Flask(__name__)


@app.route("/")
def hello():

    html = "<h3>Hello {name}!</h3>"

    filename = sys.argv[1]
    file = open(filename, "r")
    for line in file:
		html += "</br>" + line       
    return html.format(name=os.getenv("NAME", "world"))

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=80)