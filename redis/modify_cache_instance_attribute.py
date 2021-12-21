from jdcloud_sdk.services.redis.apis.ModifyCacheInstanceAttributeRequest import ModifyCacheInstanceAttributeParameters,ModifyCacheInstanceAttributeRequest
from redisClient import *


def modifyCacheInstanceAttribute():
    client = getRedisClient()

    try:
        parameters = ModifyCacheInstanceAttributeParameters("cn-north-1", "redis-w43bi668e1c5")
        parameters.setCacheInstanceName("myredis")
        request = ModifyCacheInstanceAttributeRequest(parameters)
        resp = client.send(request)
        print(resp.request_id)
        if resp.error is not None:
            print(resp.error.code, resp.error.message)
            return
        result = resp.result
        print(result)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    modifyCacheInstanceAttribute()
