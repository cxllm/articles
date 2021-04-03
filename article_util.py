import markdown
import importlib


def to_html(name: str):
    md = get_article(name)
    content = open(f"markdown/{md['md']}")
    content = content.read()
    md["html"] = markdown.markdown(
        content,
        extensions=[
            "markdown.extensions.codehilite",  # Ref: # Ref: https://python-markdown.github.io/extensions/attr_list/
            "markdown.extensions.fenced_code",  # Ref: https://python-markdown.github.io/extensions/fenced_code
            "markdown.extensions.attr_list",  # Ref: https://python-markdown.github.io/extensions/attr_list/
            "markdown.extensions.tables",  # Ref: https://python-markdown.github.io/extensions/tables/
        ],
    )
    return md


def get_article(name: str):
    info = importlib.import_module(f"articles.{name}")
    return info.content
