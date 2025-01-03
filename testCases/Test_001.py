import os

from utilities.ReadProperties import ReadConfig
import pytest
import requests
import json



class Test001:
    @pytest.mark.skip
    def test001_url(self):
        url = ReadConfig.getURL() + '/api-clients/'
        print(url)
        jsonfile = os.path.abspath(os.curdir) + '\\testData\\APIAuthentication.json'
        file = open(jsonfile, "r")
        dataInput = json.loads(file.read())
        response = requests.post(url, json=dataInput)
        print(response.status_code)
        jsonBody = json.loads(response.text)
        tokenJsonfile = os.path.abspath(os.curdir) + '\\testData\\token.json'
        newfile = open(tokenJsonfile, 'w')
        newfile.write(response.text)
        newfile.close()
