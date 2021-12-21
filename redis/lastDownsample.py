from jdcloud_sdk.core.credential import Credential
from jdcloud_sdk.services.monitor.client import MonitorClient
from jdcloud_sdk.services.monitor.apis.LastDownsampleRequest import LastDownsampleParameters, LastDownsampleRequest
from jdcloud_sdk.core.logger import Logger


access_key = ''
secret_key = ''
regionId = 'cn-north-1'
metric = 'jmiss.redis.cluster.net_io_in_per_sec'
serviceCode = 'redis'
resourceId = ''


def getMonitorClient(accessKey, secretKey):
    credential = Credential(accessKey, secretKey)
    logger = Logger(2)
    client = MonitorClient.MonitorClient(credential, logger=logger)
    return client


def lastDownsample(regionId, metric, serviceCode, resourceId):
    client = getMonitorClient(access_key, secret_key)
    try:
        parameters = LastDownsampleParameters(regionId, metric, serviceCode, resourceId)
        request = LastDownsampleRequest(parameters)
        resp = client.send(request)
        if resp.error is not None:
            print(resp.error.code, resp.error.message)
            return
        result = resp.result
        print(result)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    lastDownsample(regionId, metric, serviceCode, resourceId)