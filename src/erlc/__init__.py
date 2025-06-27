from erlc.classes.client import ( Client, UnfinishedClient )

def getconfig():
    return config
def setconfig(new):
    global config
    config = new
config = UnfinishedClient()

exports = [Client, getconfig, setconfig] # change this instead of __all__!
__all__ = exports