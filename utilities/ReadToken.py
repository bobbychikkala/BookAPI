
import json
import os


def accessToken():
    path = os.path.abspath(os.curdir)+"\\testData\\token.json"
    file = open(path, "r")
    token = file.read()
    accessToke = json.loads(token)

    return accessToke["accessToken"]