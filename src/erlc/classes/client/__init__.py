from erlc.methods.printDebug import printDebug as printDebugORIGIN
from erlc.methods.getPlayers import getPlayers as getPlayers
from erlc.logging import Logger
class Client():
    def __init__(self, globalToken: bool | None,
                 debug: bool = False):
        self.globalToken = globalToken
        
        self.logger = Logger(debug=debug)
    
    def _printDebug(self) -> None:
        return printDebugORIGIN(self)
    
    def playerCount(self, key: str) -> int:
        return playerCountORIGIN(self, key)
    

exports = [Client]
__all__ = exports