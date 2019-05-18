from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/dict", methods=["POST"])
def register():
    import main
    
    if not request.form.get("domain"):
        return render_template("failure.html")
    sphere = request.form.get("domain")

    dict = main.get_dict(sphere)

    return render_template("created_dict.html", dict_type=sphere, dict_len=range(len(dict)), dict=dict)
    


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8080)