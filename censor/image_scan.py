from jdcloud_sdk.services.censor.apis.ImageScanRequest import ImageScanRequest, ImageScanParameters
from censor_client import *


def imageScan():
    client = getCensorClient()
    try:
        parameters = ImageScanParameters()
        parameters.setScenes()

        request = ImageScanRequest(parameters)
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
    imageScan()