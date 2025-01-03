import os.path

import pytest
import requests
import json
from requests.auth import AuthBase

from utilities.ReadProperties import ReadConfig
from utilities.ReadToken import accessToken
from utilities.ReadJsonFile import ReadJsonFile

class Test_002:
    token = accessToken()
    baseURL= ReadConfig.getURL()
    headers = {"Authorization": f"Bearer {token}"}
    orderID=''

    def test_002_Post(self):
        data={
            "bookId": 1,
            "customerName": "John"
        }
        file = os.path.abspath(os.curdir) + "\\testData\\order.json"
        jsonData = ReadJsonFile.read_JsonData(self,path=file)
        #dataJson = json.loads(data.text)
        url = self.baseURL + "/orders"
        response = requests.post(url,json = jsonData,headers=self.headers)
        responseBody = json.loads(response.text)
        print(responseBody)
        assert response.status_code == 201
        Test_002.orderID = responseBody['orderId']
        assert responseBody['created'] == True



    #@pytest.mark.skip
    def test_002_GetOrders(self):
        url =self.baseURL+"/orders/"+Test_002.orderID
        response=requests.get(url,headers=self.headers)
        print(response.text)
        responseBody = response.json()
        assert responseBody['customerName'] == "John"
        assert response.status_code == 200
        print(responseBody.get("customerName"))

    #@pytest.mark.skip
    def test_002_Patch(self):
        url = self.baseURL + "/orders/" + Test_002.orderID
        data = {
            "bookId": 1,
            "customerName": "Bobby"
        }
        response = requests.patch(url, headers=self.headers,json=data)

    #@pytest.mark.skip
    def test_002_GetOrders_2(self):
        url = self.baseURL+"/orders/"+Test_002.orderID
        response = requests.get(url,headers=self.headers)
        responseBody = response.json()
        print(type(responseBody))
        assert responseBody['customerName'] =="Bobby"
        assert response.status_code == 200

    #@pytest.mark.skip
    def test_002_DeletOrders(self):
        url = self.baseURL+"/orders/"+Test_002.orderID
        response = requests.delete(url,headers=self.headers)

        #responseBody = response.json()
        print(response.text)
        #assert responseBody['customerName'] =="Bobby"
        assert response.status_code == 204


