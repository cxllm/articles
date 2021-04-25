import importlib


def get_article(name: str):
    info = importlib.import_module(f"articles.{name}")
    return info.content