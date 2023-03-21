from jdcloud_sdk.services.monitor.apis.DescribeMetricDataRequest import DescribeMetricDataParameters, DescribeMetricDataRequest
from jdcloud_sdk.services.monitor.models.TagFilter import TagFilter
from jdcloud_sdk.services.monitor.client.MonitorClient import MonitorClient
from jdcloud_sdk.core.credential import Credential
from jdcloud_sdk.core.logger import Logger
from jdcloud_sdk.core.logger import ERROR
from jdcloud_sdk.core.config import Config
from jdcloud_sdk.core.const import SCHEME_HTTPS
from jdcloud_sdk.core.const import SCHEME_HTTP
import json


regionId = 'cn-east-2'
# metric = 'vm.gpu.util.gpu'
metric = 'vm.gpu.util.mem'
serviceCode = 'vm'
resourceId = ''
startTime = '2023-03-17T00:00:00Z'
endTime = '2023-03-17T01:00:00Z'


def getGpuMonitor():
    access_key = ''
    secret_key = ''
    credential = Credential(access_key=access_key, secret_key=secret_key)
    config = Config(endpoint='monitor.jdcloud-api.com', scheme=SCHEME_HTTPS, timeout=10)
    client = MonitorClient(credential=credential, config=config, logger=Logger(ERROR))
    try:
        parameters = DescribeMetricDataParameters(regionId, metric, resourceId)
        parameters.setStartTime(startTime)
        parameters.setEndTime(endTime)
        parameters.setServiceCode(serviceCode)
        parameters.setDimension("vm-gpu")
        parameters.setGroupBy(True)

        parameters.setAggrType("avg")

        tagFilter = TagFilter("gpu_index", [0, 1, 2, 3, 4, 5, 6, 7])
        parameters.setTags([tagFilter])

        request = DescribeMetricDataRequest(parameters)
        resp = client.send(request)
        print(resp.request_id)
        if resp.error is not None:
            print(resp.error.code, resp.error.message)
            return
        print(json.dumps(resp.result))
    except Exception as e:
        print(e)


if __name__ == "__main__":
    getGpuMonitor()
