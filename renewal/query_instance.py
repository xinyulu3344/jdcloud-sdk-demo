from jdcloud_sdk.services.renewal.apis.QueryInstanceRequest import QueryInstanceParameters, QueryInstanceRequest
from jdcloud_sdk.services.renewal.models.QueryInstanceParam import QueryInstanceParam
from renewlalClient import *


def queryInstance():
    client = getRenewalClient()

    try:
        parameters = {
            "queryInstanceParam": {
                "appCode": "jcloud",
                "serviceCode": "vm",
                "instanceId": "i-71hr9codvq",
                "renewStatus": "ALL",
                "pageNumber": 1,
                "pageSize": 10
            },
            "regionId": "cn-north-1"
        }
        request = QueryInstanceRequest(parameters)
        resp = client.send(request)
        print(resp.request_id)
        if resp.error is not None:
            print(resp.error.code, resp.error.message)
            return
        result = resp.result
        print(result)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    queryInstance()
