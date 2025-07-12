from erlc.methods.printDebug import printDebug as printDebugORIGIN
from erlc.methods.playerCount import playerCount as playerCountORIGIN
from erlc.logging import Logger
class Client():
    def __init__(self, globalToken: bool | None):
        self.globalToken = globalToken
        
        self.logger = Logger(debug=False) # later on change this to be an arg
    
    def printDebug(self):
        printDebugORIGIN(self)
    
    def playerCount(self, key: str):
        playerCountORIGIN(self, key)
    

exports = [Client]
__all__ = exports