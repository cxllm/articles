from datetime import datetime
import sys
from get_article import get_article
import glob
import os

args = sys.argv
article_name = args[1]
article = glob.glob(f"{os.getcwd()}/articles/**/**/**/{article_name}.py")[0]
directory = article
article = article.split(os.getcwd())[1]
arr = article.split("/")
del arr[0]
article = ".".join(arr).split(".py")[0].split("articles.")[1]

article = get_article(article)
print(article)


def get_date():
    days = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]
    time = datetime.now()
    time = time.strftime(f"{days[time.weekday()]}, %d %B %Y")
    if article["published"]:
        article["updated"] = time
    else:
        article["published"] = time
    return time


print(get_date())
with open(directory, "w", encoding="utf-8") as f:
    f.write(f"content={article}")
