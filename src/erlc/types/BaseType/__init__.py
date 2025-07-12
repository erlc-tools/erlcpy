class BaseType:
    raw: str | list | dict | int | bool # Original input
    
    class Value: # This will be the actual value of the thing
        ...
    
    def create(self, *args):
        print("ERLC-PY WARNING: BaseType.create was called.")