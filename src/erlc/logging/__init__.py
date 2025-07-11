debug: bool = True
if debug:
    from icecream import ic


def error(content):
    print(f"ERROR: {content}")
def debug(*args):
    if debug:
        ic("ERLC-PY DEBUG", args)