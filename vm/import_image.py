from jdcloud_sdk.services.vm.apis.ImportImageRequest import ImportImageParameters, ImportImageRequest
from vmClient import *


def importImage(regionId, architecture, osType, platform, diskFormat, systemDiskSizeGB, imageUrl, imageName):
    client = getVmClient()
    try:
        parameters = ImportImageParameters(regionId, architecture, osType, platform, diskFormat, systemDiskSizeGB,
                                           imageUrl, imageName)
        request = ImportImageRequest(parameters)
        resp = client.send(request)
        print("requestId: ", resp.request_id)
        if resp.error is not None:
            print(resp.error.code, resp.error.message)
            return
        print(resp.result)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    importImage("cn-north-1", "", "", "", "", "", "", "")
