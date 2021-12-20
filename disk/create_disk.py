from jdcloud_sdk.services.disk.apis.CreateDisksRequest import CreateDisksRequest
from diskClient import *


def createDisk():
    client = getDiskClient()
    try:
        request = CreateDisksRequest({
            "clientToken": "xxxxxxxx",
            "maxCount": 1,
            "diskSpec": {
                "diskSizeGB": 20,
                "diskType": "hdd",
                "name": "apitest",
                "charge": {
                    "chargeMode": "postpaid_by_duration",
                    # "chargeUnit": "month",
                    # "chargeDuration": 1,
                    "autoRenew": False
                },
                "az": "cn-north-1a"
            },
            "regionId": "cn-north-1"
        })
        resp = client.send(request)
        if resp.error is not None:
            print(resp.error.code, resp.error.message)
            return
        result = resp.result
        print(result)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    createDisk()
