from icecream import ic
from requests import get
from erlc.logging import error, debug

def playerCount(client, key: str):
    res = get("https://api.policeroleplay.community/v1/server/players",
              headers={
                  "Authorization": client.globalToken,
                  "Server-Key": key
              } if client.globalToken else {
                  "Server-Key": key
              })
    try:
        return len(res.json())
    except:
        error("Failed to parse response json from playerCount.")
        debug(res.json(), key, client.globalToken)