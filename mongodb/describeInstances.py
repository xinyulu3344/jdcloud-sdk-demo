from jdcloud_sdk.services.mongodb.apis.DescribeInstancesRequest import DescribeInstancesRequest,DescribeInstancesParameters
from jdcloud_sdk.services.common.models.Filter import Filter
from mongodbClient import *


def describeInstances():
    client = getMongodbClient()

    try:
        parameters = DescribeInstancesParameters("cn-north-1")
        parameters.setFilters([Filter(name="instanceId", values=["mongo-0i770e9byp"], operator="eq")])
        request = DescribeInstancesRequest(parameters)
        resp = client.send(request)
        print(resp.request_id)
        if resp.error is not None:
            print(resp.error.code, resp.error.message)
            return
        print(resp.result)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    describeInstances()
