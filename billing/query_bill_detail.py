from jdcloud_sdk.services.billing.apis.QueryBillDetailRequest import QueryBillDetailParameters, QueryBillDetailRequest
from billingClient import *


def queryBillingDetail():
    client = getBillingClient()
    try:
        parameters = QueryBillDetailParameters("cn-north-1", "2021-05-31 00:00:00", "2021-05-31 23:59:59")
        parameters.setPageSize(10)
        parameters.setPageIndex(1)
        parameters.setServiceCode("vm")
        parameters.setResourceIds([""])
        request = QueryBillDetailRequest(parameters)
        resp = client.send(request)
        print(resp.request_id)
        if resp.error is not None:
            print(resp.error.code, resp.error.message)
            return
        print(resp.result)

    except Exception as e:
        print(e)


if __name__ == "__main__":
    queryBillingDetail()
