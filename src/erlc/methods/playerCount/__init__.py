from icecream import ic
from requests import get

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
        pass # error