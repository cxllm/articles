import importlib


def get_article(name: str):
    try:
        info = importlib.import_module(f"articles.{name}").content
    except ModuleNotFoundError:
        info = None
    return info
