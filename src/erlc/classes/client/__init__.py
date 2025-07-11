from erlc.methods.printDebug import printDebug as printDebugORIGIN
class Client():
    def __init__(self, globalToken: bool | None):
        self.globalToken = globalToken
    
    def printDebug(self):
        printDebugORIGIN(self)
    

exports = [Client]
__all__ = exports