from jdcloud_sdk.services.rds.apis.CreateDatabaseRequest import CreateDatabaseParameters,CreateDatabaseRequest
from jdcloud_sdk.services.rds.apis.GrantPrivilegeRequest import GrantPrivilegeParameters,GrantPrivilegeRequest
from jdcloud_sdk.services.rds.models.AccountPrivilege import AccountPrivilege
from rdsClient import *


def createDatabase():
    client = getRdsClient()

    try:
        parameters = CreateDatabaseParameters("cn-north-1", "mysql-ykdunggylk", "mydb", "utf8mb4")

        request = CreateDatabaseRequest(parameters)
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
    createDatabase()
