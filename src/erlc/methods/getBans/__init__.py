from icecream import ic
from requests import get

def getBans(client, key: str):
    res = get("https://api.policeroleplay.community/v1/server/bans",
              headers={
                  "Authorization": client.globalToken,
                  "Server-Key": key
              } if client.globalToken else {
                  "Server-Key": key
              })
    try:
        return res.json()
    except:
        client.logger.error("Failed to parse response json from getBans.")
        client.logger.debug(res.json(), key, client.globalToken)