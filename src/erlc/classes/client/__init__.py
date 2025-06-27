class Client():
    def __init__(self, options: dict):
        if not isinstance(options, dict):
            raise TypeError(f"Expected dict for parameters options. Got {type(options)}")
            return
        
        self.options = options
    
    def config(self, silence: bool = False):
        if not silence:
            print(f"WARNING: The config function in Client is not required to call. Pass silence=True to stop this warning.") # TODO: add color
        return self.options