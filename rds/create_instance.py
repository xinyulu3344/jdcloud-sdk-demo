from jdcloud_sdk.services.rds.apis.CreateInstanceRequest import CreateInstanceParameters, CreateInstanceRequest
from jdcloud_sdk.services.rds.apis.CreateInstanceFromBackupRequest import CreateInstanceFromBackupParameters, \
    CreateInstanceFromBackupRequest
from jdcloud_sdk.services.rds.models.DBInstanceSpec import DBInstanceSpec
from jdcloud_sdk.services.charge.models.ChargeSpec import ChargeSpec
from rdsClient import *


def createInstance():
    # 获取RDS的client
    client = getRdsClient()
    # 设置计费参数，默认是按配置计费
    chargeSpec = ChargeSpec()
    chargeSpec.chargeMode = "postpaid_by_duration"

    # 设置实例参数
    instanceSpec = DBInstanceSpec(engine="MySQL",
                                  engineVersion="5.7",
                                  instanceClass="db.mysql.s1.micro",
                                  instanceStorageGB=40,
                                  azId=["cn-north-1a"],
                                  vpcId="vpc-nutq6o7xvs",
                                  subnetId="subnet-bdez5h8w59",
                                  chargeSpec=chargeSpec,
                                  instanceName="sdk_test",
                                  parameterGroup=None)

    try:
        parameters = CreateInstanceParameters("cn-north-1", instanceSpec=instanceSpec)
        request = CreateInstanceRequest(parameters)
        resp = client.send(request)

        print("requestId: ", resp.request_id)

        # 错误处理
        if resp.error is not None:
            print(resp.error.code, resp.error.message)
            return

        print("创建RDS实例：", resp.result)
    except Exception as e:
        print(e)


def createInstanceFromBack():
    client = getRdsClient()
    chargeSpec = ChargeSpec()
    chargeSpec.chargeMode = "postpaid_by_duration"
    instanceSpec = DBInstanceSpec(engine="MySQL",
                                  engineVersion="5.7",
                                  instanceClass="db.mysql.s1.micro",
                                  instanceStorageGB=40,
                                  azId=["cn-north-1a"],
                                  vpcId="vpc-nutq6o7xvs",
                                  subnetId="subnet-bdez5h8w59",
                                  chargeSpec=chargeSpec,
                                  instanceName="sdk_test",
                                  parameterGroup=None)
    try:
        parameters = CreateInstanceFromBackupParameters("cn-north-1", "e02535e7-29ad-4362-ba35-112f762e64c9", "MySQL", instanceSpec)
        request = CreateInstanceFromBackupRequest(parameters)
        resp = client.send(request)

        print("requestId: ", resp.request_id)

        # 错误处理
        if resp.error is not None:
            print(resp.error.code, resp.error.message)
            return

        print(resp.result)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    # createInstance()
    createInstanceFromBack()
