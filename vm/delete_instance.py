from jdcloud_sdk.services.vm.apis.DeleteInstanceRequest import DeleteInstanceParameters, DeleteInstanceRequest
from vmClient import *


def deleteInstance():
    client = getVmClient()

    try:
        parameters = DeleteInstanceParameters("cn-north-1", "")

        request = DeleteInstanceRequest(parameters)
        resp = client.send(request)
        print(resp.request_id)
        if resp.error is not None:
            print(resp.error.code, resp.error.message)
            return
        print(resp.result)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    deleteInstance()
