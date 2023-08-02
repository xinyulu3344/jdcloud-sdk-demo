from jdcloud_sdk.services.ag.apis.EnableAutoScalingRequest import EnableAutoScalingParameters, EnableAutoScalingRequest
from jdcloud_sdk.services.ag.models.AutoscalingSpec import AutoscalingSpec
from agClient import *

def enableAutoScaling(regionId, agId, isManaged):
    client = getAgClient()
    try:
        parameter = EnableAutoScalingParameters(regionId, agId)
        parameter.setIsManaged(isManaged)

        autoscalingSpec = AutoscalingSpec(minSize=0, maxSize=1, desiredCapacity=0, healthCheck=True, coolDownSeconds=300, scalingPolicy='Balance', removalPolicy='OldestResource')
        parameter.setAutoscalingSpec(autoscalingSpec)

        request = EnableAutoScalingRequest(parameter)
        resp = client.send(request)
        if resp.error is not None:
            print(resp.error.code, resp.error.message)
            return
        print(resp)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    enableAutoScaling("cn-north-1", "", False)