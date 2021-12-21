from jdcloud_sdk.services.rds.apis.CreateAccountRequest import CreateAccountParameters, CreateAccountRequest
from rdsClient import *


def create_account():
    client = getRdsClient()
    try:
        parameters = CreateAccountParameters("cn-north-1", "mysql-ykdunggylk", "mytest", "Jdcloud123!!")
        request = CreateAccountRequest(parameters)
        resp = client.send(request)
        print("request_id: ", resp.request_id)
        if resp.error is not None:
            print(resp.error.code, resp.error.message)
            return
        print(resp.result)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    create_account()
