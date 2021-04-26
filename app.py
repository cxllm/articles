from flask import Flask, render_template, request, redirect
import os
import glob
import markdown
from get_article import get_article


def format_articles(article: str):
    article = article.split(os.getcwd())[1]
    arr = article.split("/")
    del arr[0]
    article = ".".join(arr).split(".py")[0].split("articles.")[1]
    info = get_article(article)
    return info


articles = glob.glob(f"{os.getcwd()}/articles/**/**/**/*")
print(articles)
try:
    for i in range(len(articles)):
        if "__pycache__" in articles[i]:
            del articles[i]
        print(articles)
except:
    None
articles = list(map(format_articles, articles))  #

app = Flask(__name__, static_url_path="/public/", static_folder="public")


@app.route("/")
def root():
    return render_template("index.html", articles=articles)


@app.route("/<string:article>")
def article_route(article):
    try:
        article = to_html(article)
        return render_template("article.html", content=article)
    except:
        page_not_found("Error")


@app.route("/favicon.ico")
def favicon():
    return redirect("https://cxllm.xyz/favicon.ico")


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html", path=request.path)


extension_configs = {"codehilite": {"use_pygments": True}}


def to_html(article: str):
    found = None
    for i in articles:
        if i["endpoint"] == article.lower():
            found = i
            break
        else:
            continue
    if not found:
        raise FileNotFoundError("Not Found")
    try:
        found["html"]
    except:
        content = open(f"markdown/{found['md']}")
        content = content.read()
        html = markdown.markdown(
            content,
            extensions=[
                "markdown.extensions.codehilite",  # Ref: # Ref: https://python-markdown.github.io/extensions/attr_list/
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
