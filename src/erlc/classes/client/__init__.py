class Client():
    def __init__(self, globalToken: bool | None):
        self.globalToken = globalToken
    

exports = [Client]
__all__ = exports