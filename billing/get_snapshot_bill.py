from jdcloud_sdk.services.billing.apis.QueryBillDetailRequest import QueryBillDetailParameters, QueryBillDetailRequest
from billingClient import *


def get_snapshot_bill():
    client = getBillingClient()
    try:
        parameters = QueryBillDetailParameters("cn-north-1", "2022-08-24 00:00:00", "2022-08-24 23:59:59")
        parameters.setPageSize(10)
        parameters.setPageIndex(1)
        parameters.setServiceCode("snapshot")
        request = QueryBillDetailRequest(parameters)
        resp = client.send(request)
        print(resp.request_id)
        if resp.error is not None:
            print(resp.error.code, resp.error.message)
            return
        for item in resp.result['result']:
            print(item['startTime'], item['endTime'], item['region'], item['formula'], item['totalFee'])

    except Exception as e:
        print(e)


if __name__ == "__main__":
    get_snapshot_bill()
