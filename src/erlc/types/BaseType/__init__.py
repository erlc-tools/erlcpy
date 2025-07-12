class BaseType:
    def __init__(self):
        self.value = self.Value()
    raw: any # Original input
    
    class Value: # This will be the actual value of the thing
        ...
    
    def create(*args):
        print("ERLC-PY WARNING: BaseType.create was called.")
        
        new = BaseType()
        new.raw = args
        return new