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
        
    def getBans(self, key: str) -> dict[str: str]:
        ...
    
    def getCommandLogs(self, key: str) -> list[dict]:
        ...
        
    def getJoinLogs(self, key: str) -> list[dict]:
        ...
        
    def getKillLogs(self, key: str) -> list[dict]:
        ...
    
    def getModcallLogs(self, key: str) -> list[dict]:
        ...
    
    def getQueue(self, key: str) -> list[int]:
        ...
        

exports = [Client]
__all__ = exports