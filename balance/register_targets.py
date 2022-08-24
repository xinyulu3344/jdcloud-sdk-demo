from jdcloud_sdk.services.lb.apis.RegisterTargetsRequest import RegisterTargetsParameters,RegisterTargetsRequest
from jdcloud_sdk.services.lb.models.TargetSpec import TargetSpec
from lbClient import *


def registerTargets():
    client = getLbClient()

    try:
        # targetSpecs = [{
        #     "instanceId": "云主机id1",
        #     "type": "vm",
        #     "port": 80,
        #     "weight": 10,
        # }, {
        #     "instanceId": "云主机id2",
        #     "type": "vm",
        #     "port": 80,
        #     "weight": 10,
        #
        # }]
        # parameters = RegisterTargetsParameters("cn-north-1", "", targetSpecs)

        parameters = RegisterTargetsParameters("", "", [TargetSpec(), TargetSpec()])

        request = RegisterTargetsRequest(parameters)
        resp = client.send(request)
        print(resp.request_id)
        if resp.error is not None:
            print(resp.error.code, resp.error.message)
            return
        print(resp.result)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    registerTargets()