class Client():
    def __init__(self, options: dict):
        if not isinstance(options, dict):
            raise TypeError(f"Expected dict for parameters options. Got {type(options)}")
            return
        
        self.options = options
    
    def config(self):
        return self.options