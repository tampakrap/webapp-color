from flask import Flask
from flask import render_template
import socket
import random
import os
import argparse

app = Flask(__name__)

color_codes = {
    "red": "#e74c3c",
    "green": "#16a085",
    "blue": "#2980b9",
    "blue2": "#30336b",
    "pink": "#be2edd",
    "darkblue": "#130f40",
    "white": "#e4e4e4",
}

SUPPORTED_COLORS = ",".join(color_codes.keys())

# Get background color from Environment variable
BG_COLOR_FROM_ENV = os.environ.get('BG_COLOR')
# Default background color
BG_COLOR = "blue"

# Get text color from Environment variable
TEXT_COLOR_FROM_ENV = os.environ.get('TEXT_COLOR')
# Default background color
TEXT_COLOR = "white"



@app.route("/")
def main():
    # return 'Hello'
    return render_template('hello.html', name=socket.gethostname(), bg_color=color_codes[BG_COLOR], text_color=color_codes[TEXT_COLOR])


if __name__ == "__main__":

    print(" This is a sample web application that displays a colored background and text. \n"
          " A color can be specified as an Environment variable BG_COLOR and TEXT_COLOR. Accepts one of " + SUPPORTED_COLORS + " \n"
          "")

    if BG_COLOR_FROM_ENV:
        print("No Command line argument for BG_COLOR. Color from environment variable " + BG_COLOR_FROM_ENV)
        BG_COLOR = BG_COLOR_FROM_ENV
    else:
        print("No command line argument or environment variable for BG_COLOR. Using the default color " + BG_COLOR)

    # Check if input color is a supported one
    if BG_COLOR not in color_codes:
        print("Color not supported. Received '" + BG_COLOR + "' expected one of " + SUPPORTED_COLORS)
        exit(1)

    if TEXT_COLOR_FROM_ENV:
        print("No Command line argument for TEXT_COLOR. Color from environment variable " + TEXT_COLOR_FROM_ENV)
        TEXT_COLOR = TEXT_COLOR_FROM_ENV
    else:
        print("No command line argument or environment variable for TEXT_COLOR. Using the default color " + TEXT_COLOR)

    # Check if input color is a supported one
    if TEXT_COLOR not in color_codes:
        print("Color not supported. Received '" + TEXT_COLOR + "' expected one of " + SUPPORTED_COLORS)
        exit(1)


    # Run Flask Application
    app.run(host="0.0.0.0", port=8080)
