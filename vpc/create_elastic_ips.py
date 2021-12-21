from jdcloud_sdk.services.vpc.apis.CreateElasticIpsRequest import CreateElasticIpsRequest
from vpcClient import *


# 创建弹性公网ip
def createElasticIps():
    client = getVpcClient()
    try:
        # 创建弹性公网ip参数
        parameters = {
            "maxCount": 1,
            "elasticIpSpec": {
                "provider": "bgp",
                "bandwidthMbps": 1,
                "chargeSpec": {
                    "chargeMode": "postpaid_by_duration"
                }
            },
            "regionId": "cn-north-1"
        }

        request = CreateElasticIpsRequest(parameters)
        resp = client.send(request)
        print("requestId: ", resp.request_id)
        if resp.error is not None:
            print(resp.error.code, resp.error.message)
            return
        result = resp.result
        print(result)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    createElasticIps()
