import json


class ReadJsonFile():
    @staticmethod
    def read_JsonData(self,path):
        jsonFilePath = path
        jsonfile = open(jsonFilePath)
        jsonData = json.loads(jsonfile.read())
        return jsonData