from jdcloud_sdk.services.iam.apis.DescribeSubUsersRequest import DescribeSubUsersParameters, DescribeSubUsersRequest
from iamClient import *


def describeSubUsers():
    client = getIamClient()
    try:
        parameters = DescribeSubUsersParameters()
        parameters.setPageNumber(1)
        parameters.setPageSize(100)

        request = DescribeSubUsersRequest(parameters)
        resp = client.send(request)
        print(resp.request_id)
        if resp.error is not None:
            print(resp.error.code, resp.error.message)
            return
        print(resp.result)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    describeSubUsers()
