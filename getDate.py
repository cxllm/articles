from datetime import datetime
import sys
from get_article import get_article

args = sys.argv
article_name = args[1]

article = get_article(article_name)

print(article)


def getDate():
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
    time = time.strftime(f"{days[time.weekday()]}, %d %b %Y")
    if article["published"]:
        article["updated"] = time
    else:
        article["published"] = time
    return time


print(getDate())
f = open(f"articles/{article_name}.py", "w")
f.write(f"content={article}")