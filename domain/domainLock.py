from jdcloud_sdk.services.domain.apis.DomainLockRequest import DomainLockParameters, DomainLockRequest
from jdcloud_sdk.services.domain.apis.DomainUnLockRequest import DomainUnLockParameters, DomainUnLockRequest
from domainClient import *


def domainLock():
    client = getDomainClient()
    try:
        parameters = DomainLockParameters("cn-north-1", "")
        request = DomainLockRequest(parameters)
        resp = client.send(request)
        print(resp.request_id)
        if resp.error is not None:
            print(resp.error.code, resp.error.message)
            return
        print(resp.result)
    except Exception as e:
        print(e)

def domainUnlock():
    client = getDomainClient()
    try:
        parameters = DomainUnLockParameters("cn-north-1", "")
        request = DomainUnLockRequest(parameters)
        resp = client.send(request)
        print(resp.request_id)
        if resp.error is not None:
            print(resp.error.code, resp.error.message)
            return
        print(resp.result)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    # domainLock()
    domainUnlock()
