from jdcloud_sdk.services.iam.apis.DeletePolicyRequest import DeletePolicyParameters, DeletePolicyRequest
from iamClient import *


def deletePolicyTest(policyName):
    client = getIamClient()
    try:
        parameters = DeletePolicyParameters(policyName)
        request = DeletePolicyRequest(parameters)
        resp = client.send(request)
        print(resp.request_id)
        if resp.error is not None:
            print(resp.error.code, resp.error.message)
            return
        print(resp.result)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    deletePolicyTest("test")
