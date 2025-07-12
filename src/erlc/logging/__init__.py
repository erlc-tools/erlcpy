class Logger():
    def __init__(self, debug: bool = False):
        if debug:
            from icecream import ic
            self._ic = ic # allow for use outside of the class
    
    def error(self, content):
        print(f"ERROR: {content}")
        
    def debug(self, *args):
        if self.debug:
            self._ic("ERLC-PY DEBUG", args)