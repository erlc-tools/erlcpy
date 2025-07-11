from erlc.methods.printDebug import printDebug as printDebugORIGIN
from erlc.methods.playerCount import playerCount as playerCountORIGIN
class Client():
    def __init__(self, globalToken: bool | None):
        self.globalToken = globalToken
    
    def printDebug(self):
        printDebugORIGIN(self)
    
    def playerCount(self, key: str):
        playerCountORIGIN(self, key)
    

exports = [Client]
__all__ = exports