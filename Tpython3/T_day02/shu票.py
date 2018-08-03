# coding=utf-8
import requests

ip = "https://service.16hour.cn"
port = ":29529"
link = "/AppSixteenHour.ashx/GetPushListByPlateID"
data = {"PlateID": 7, "PageIndex": 1, "PageSize": 600, "TelePhone": 15680905350, "City": "成都市"}
req = requests.post(ip + port + link, json=data)
print(req.text)
