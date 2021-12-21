from jdcloud_sdk.services.resourcetag.apis.TagResourcesRequest import TagResourcesParameters, TagResourcesRequest
from jdcloud_sdk.services.resourcetag.models.TagResourcesReqVo import TagResourcesReqVo
from jdcloud_sdk.services.resourcetag.models.ResourcesMap import ResourcesMap
from resourcetagClient import *

regionId = "cn-north-1"
serviceCode = "redis"
resourceIds = ["redis-w43bi668e1c5"]
tags = [{"key": "mykey", "value": "myvalue"}]


def tagResources():
    client = getResourcetagClient()
    try:
        resourceMap = ResourcesMap(serviceCode, resourceIds)
        tagResources = TagResourcesReqVo([resourceMap], tags)
        parameters = TagResourcesParameters(regionId, tagResources)
        request = TagResourcesRequest(parameters)
        resp = client.send(request)
        print(resp.request_id)
        if resp.error is not None:
            print(resp.error.code, resp.error.message)
            return
        print(resp.result)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    tagResources()
