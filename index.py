from flask import Flask, render_template, request
from article_util import to_html, get_article
import os
import glob


def format_articles(article: str):
    article = article.split(os.getcwd())[1]
    arr = article.split("/")
    del arr[0]
    article = ".".join(arr).split(".py")[0].split("articles.")[1]
    info = get_article(article)
    info["endpoint"] = f"a/{article}"
    return info


articles = glob.glob(f"{os.getcwd()}/articles/*")
try:
    del articles[articles.index(f"{os.getcwd()}/articles/__pycache__")]
except:
    None
articles = list(map(format_articles, articles))

app = Flask(__name__, static_url_path="/public/", static_folder="public")


@app.route("/")
def root():
    return render_template("index.html", articles=articles)


@app.route("/a/<string:article>")
def article_route(article):
    try:
        article = to_html(article)
        return render_template("article.html", content=article)
    except:
        return page_not_found("e")


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html", path=request.path)


app.run(port=9756)
