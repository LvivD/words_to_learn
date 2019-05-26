from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route("/")
def index():
    """
    First main page.
    """
    return render_template("index.html")


@app.route("/dict", methods=["POST"])
def register():
    """
    Page with dictionary.
    """
    import modules.main

    if not request.form.get("sphere") or not request.form.get("words_num") or not request.form.get("articles_num"):
        return render_template("failure.html", Error='Wrong input!')
    sphere = request.form.get("sphere")
    number_of_words = int(request.form.get("words_num"))
    number_of_articles = int(request.form.get("articles_num"))

    dct = modules.main.get_dict_from_NYT(sphere,
                                         num_of_words_to_return=number_of_words,
                                         num_of_articles_to_study=number_of_articles)

    return render_template("created_dict.html", dict_type=sphere, dict_len=list(range(len(dct))), dict=set(dct))


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8080)
