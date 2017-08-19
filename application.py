from flask import Flask, redirect, request, session, render_template

request_counter = {"GET": 0, "POST": 0, "PUT": 0, "DELETE": 0}

app = Flask(__name__)

@app.route("/request-counter", methods=["GET", "POST", "PUT", "DELETE"])
def route_request_counter():
    if request.method in request_counter:
        request_counter[request.method] += 1
                
    with open("request_counts.txt", "w") as f:
        for i in request_counter:
            line = i + ":" + str(request_counter[i]) + "\n"
            f.write(line)
 
    return render_template("form.html")

@app.route("/statistics", methods=["GET"])
def route_statistics():
    content_to_render = []
    with open("request_counts.txt", "r") as f:
        for line in f:
            line = line.split(":")
            content_to_render.append(line)
    return render_template("statistics.html", content=content_to_render)


if __name__ == "__main__":
    app.secret_key = "app_magic"  # Change the content of this string
    app.run(
        debug=True,
        port=5000
    )


