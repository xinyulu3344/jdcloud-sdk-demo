from jdcloud_sdk.services.monitor.client.MonitorClient import MonitorClient
from jdcloud_sdk.core.credential import Credential
from jdcloud_sdk.core.logger import Logger
from jdcloud_sdk.core.logger import ERROR
from jdcloud_sdk.core.config import Config
from jdcloud_sdk.core.const import SCHEME_HTTPS
from jdcloud_sdk.services.monitor.apis.PutMetricDataRequest import PutMetricDataParameters, PutMetricDataRequest
from jdcloud_sdk.services.monitor.models.MetricDataCm import MetricDataCm


def getMonitorClient():
    credential = Credential(access_key="", secret_key="")
    config = Config(endpoint='monitor.cn-east-2.jdcloud-api.com', scheme=SCHEME_HTTPS, timeout=10)
    client = MonitorClient(credential=credential, config=config, logger=Logger(ERROR))
    return client


def putMetricData():
    client = getMonitorClient()
    metricDataList = [
        MetricDataCm(
            namespace="vm",
            metric="vm.cpu.usage1",
            dimensions={"host": "172.29.8.11", "service": "order"},
            timestamp=1690951929,
            type=1,
            values={'value': 18},
            unit=""),
    ]
    try:
        parameters = PutMetricDataParameters()
        parameters.setMetricDataList(metricDataList)

        request = PutMetricDataRequest(parameters)
        resp = client.send(request)
        print(resp.request_id)
        if resp.error is not None:
            print(resp.error.code, resp.error.message)
            return
        print(resp.result)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    putMetricData()