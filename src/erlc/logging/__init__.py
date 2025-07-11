debug: bool = True
if debug:
    from icecream import ic


def error(content):
    print(f"ERROR: {content}")
def debug(content):
    if debug:
        ic("ERLC-PY DEBUG", content)