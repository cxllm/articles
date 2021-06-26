from flask import Flask, render_template, request, redirect
import os
import glob
import markdown
from get_article import get_article
from pathlib import Path

Path(f"{os.getcwd()}/templates/articles").mkdir(parents=True, exist_ok=True)
articles = glob.glob(f"{os.getcwd()}/articles/**/**/**/*")
try:
    for i in range(len(articles) - 1):
        if "__pycache__" in articles[i]:
            del articles[i]
except IndexError:
    articles = articles
article_dirs = articles
articles = []
for article in article_dirs:
    if "__pycache__" in article:
        continue
    article = article.split(os.getcwd())[1]
    arr = article.split("/")
    del arr[0]
    article = ".".join(arr).split(".py")[0].split("articles.")[1]
    dates = arr
    del dates[0]
    info = get_article(article)
    info["year"] = dates[0]
    info["month"] = dates[1]
    info["day"] = dates[2]
    info["endpoint"] = dates[3].split(".py")[0]
    info[
        "full_endpoint"
    ] = f"/{info['year']}/{info['month']}/{info['day']}/{info['endpoint']}"
    if info is not None:
        articles.append(info)
articles.reverse()

app = Flask(__name__, static_url_path="/public/", static_folder="public")


@app.route("/")
def root():
    return render_template("index.html", articles=articles)


@app.route("/<string:year>/<string:month>/<string:day>/<string:article_name>")
def article_route(year, month, day, article_name):
    try:
        a = to_html(article_name, year, month, day)
        return render_template("article.html", content=a)
    except FileNotFoundError:
        return page_not_found("Error")


@app.route("/favicon.ico")
def favicon():
    return redirect("https://cxllm.xyz/favicon.ico")


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html", path=request.path)


extension_configs = {"codehilite": {"use_pygments": True}}


def to_html(article_name: str, year, month, day):
    found = None
    for i in articles:
        if (
            i["endpoint"] == article_name.lower()
            and i["year"] == year
            and i["month"].lower() == month.lower()
            and i["day"] == day
        ):
            found = i
            break
        else:
            continue
    if found is None:
        raise FileNotFoundError("Not Found")
    try:
        found["html"]
    except KeyError:
        content = open(f"markdown/{found['md']}")
        content = content.read()
        html = markdown.markdown(
            content,
            extensions=[
                "markdown.extensions.codehilite",  # Ref: https://python-markdown.github.io/extensions/code_hilite
                "markdown.extensions.fenced_code",  # Ref: https://python-markdown.github.io/extensions/fenced_code
                "markdown.extensions.attr_list",  # Ref: https://python-markdown.github.io/extensions/attr_list/
                "markdown.extensions.tables",  # Ref: https://python-markdown.github.io/extensions/tables/
            ],
        )
        found["html"] = found["md"].split(".md")[0] + ".html"
        f = open(f"templates/articles/{found['html']}", "w")
        f.seek(0)
        f.write(html)
        f.truncate()
        f.close()
    return found


if __name__ == "__main__":
    app.run(port=9756, debug=True)
