from erlc.methods.printDebug import printDebug as printDebugORIGIN
from erlc.methods.playerCount import playerCount as playerCountORIGIN
from erlc.logging import Logger
class Client():
    def __init__(self, globalToken: bool | None,
                 debug: bool = False):
        self.globalToken = globalToken
        
        self.logger = Logger(debug=debug)
    
    def printDebug(self) -> None:
        printDebugORIGIN(self)
    
    def playerCount(self, key: str) -> int:
        playerCountORIGIN(self, key)
    

exports = [Client]
__all__ = exports