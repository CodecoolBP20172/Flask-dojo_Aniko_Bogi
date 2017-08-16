from flask import Flask, redirect, request, session

app = Flask(__name__)


@app.route("/request-counter", methods=['GET', 'POST'])
def route_request_counter():

    return redirect(





if __name__ == "__main__":
    app.secret_key = "app_magic"  # Change the content of this string
    app.run(
        debug=True,
        port=5000
    )
