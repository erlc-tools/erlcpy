from erlc.methods.printDebug import printDebug as printDebugORIGIN
from erlc.methods.getPlayers import getPlayers as getPlayersORIGIN
from erlc.methods.getBans import getBans as getBansORIGIN
from erlc.logging import Logger
class Client():
    def __init__(self, globalToken: bool | None,
                 debug: bool = False):
        self.globalToken = globalToken
        
        self.logger = Logger(debug=debug)
    
    def _printDebug(self) -> None:
        return printDebugORIGIN(self)
    
    def getPlayers(self, key: str) -> int:
        return getPlayersORIGIN(self, key)
        
    def getBans(self, key: str) -> dict[str: str]:
        return getBansORIGIN(self, key)
    
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
    
    def runCommand(self, key: str, command: str) -> None:
        ...
        

exports = [Client]
__all__ = exports