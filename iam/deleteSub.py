from jdcloud_sdk.services.iam.apis.DeleteSubUserRequest import DeleteSubUserParameters, DeleteSubUserRequest
from iamClient import *


def deleteSubUserTest(subUser):
    client = getIamClient()
    try:
        parameters = DeleteSubUserParameters(subUser)
        request = DeleteSubUserRequest(parameters)
        resp = client.send(request)
        print(resp.request_id)
        if resp.error is not None:
            print(resp.error.code, resp.error.message)
            return
        print(resp.result)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    deleteSubUserTest("subUser")
