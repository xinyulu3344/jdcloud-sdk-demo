from jdcloud_sdk.services.ossopenapi.apis.GetSingleBucketCapacityRequest import GetSingleBucketCapacityParameters, GetSingleBucketCapacityRequest
from ossClient import *


def getSingleBucketCapacity():
    client = getOssClient()

    try:
        parameters = GetSingleBucketCapacityParameters("cn-north-1", "BUCKET", [1000040], 2)
        parameters.setPeriodType(2)

        request = GetSingleBucketCapacityRequest(parameters)
        resp = client.send(request)
        print(resp.request_id)
        if resp.error is not None:
            print(resp.error.code, resp.error.message)
            return
        print(resp.result)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    getSingleBucketCapacity()