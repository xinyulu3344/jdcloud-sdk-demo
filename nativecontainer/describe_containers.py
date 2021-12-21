from jdcloud_sdk.services.nc.apis.DescribeContainersRequest import DescribeContainersParameters, DescribeContainersRequest
from nativecontainerClient import getNativecontainerClient


def describeContainers():
    client = getNativecontainerClient()
    try:
        parameters = DescribeContainersParameters("cn-north-1")
        parameters.setPageNumber(1)
        parameters.setPageSize(20)
        request = DescribeContainersRequest(parameters)
        resp = client.send(request)
        print(resp.request_id)
        if resp.error is not None:
            print(resp.error.code, resp.error.message)
            return
        print(resp.result)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    describeContainers()
