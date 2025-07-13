from erlc.methods.printDebug import printDebug as printDebugORIGIN
from erlc.methods.getPlayers import getPlayers as getPlayers
from erlc.logging import Logger
class Client():
    def __init__(self, globalToken: bool | None,
                 debug: bool = False):
        self.globalToken = globalToken
        
        self.logger = Logger(debug=debug)
    
    def _printDebug(self) -> None:
        printDebugORIGIN(self)
    
    def getPlayers(self, key: str) -> int:
        getPlayers(self, key)
    
    
    

exports = [Client]
__all__ = exports