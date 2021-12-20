from jdcloud_sdk.services.billing.apis.QueryBillSummaryRequest import QueryBillSummaryParameters, \
    QueryBillSummaryRequest
from billingClient import *


def queryBillingSummary():
    client = getBillingClient()
    try:
        parameters = QueryBillSummaryParameters("cn-north-1", "2020-06-01 00:00:00", "2020-06-30 23:59:59")
        parameters.setPageSize(10)
        parameters.setPageIndex(1)
        parameters.setServiceCode("vm")
        parameters.setResourceIds([""])
        request = QueryBillSummaryRequest(parameters)
        resp = client.send(request)
        print(resp.request_id)
        if resp.error is not None:
            print(resp.error.code, resp.error.message)
            return
        print(resp.result)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    queryBillingSummary()
