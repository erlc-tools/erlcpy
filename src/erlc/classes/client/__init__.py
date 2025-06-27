from src.erlc import getconfig, setconfig
from classes.client.unfinishedclient import UnfinishedClient
class Client():
    def __init__(self, options: dict):
        if not isinstance(options, dict):
            raise TypeError(f"Expected dict for parameters options. Got {type(options)}")
            return
        
        self.options = options
    
    def config(self):
        setconfig(self.options)
        return self.options

exports = [Client, UnfinishedClient]
__all__ = exports