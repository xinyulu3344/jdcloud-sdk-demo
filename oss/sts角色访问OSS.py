from jdcloud_sdk.core.credential import Credential
from jdcloud_sdk.core.config import Config
from jdcloud_sdk.core.logger import Logger
from jdcloud_sdk.services.sts.client.StsClient import StsClient
from jdcloud_sdk.services.sts.models.AssumeRoleInfo import AssumeRoleInfo
from jdcloud_sdk.services.sts.apis.AssumeRoleRequest import AssumeRoleParameters, AssumeRoleRequest
import boto3


def getToken():
    logger = Logger(2)

    # 授权assumeRole的子账号ak/sk
    access_key = ''
    secret_key = ''

    credential = Credential(access_key, secret_key)
    client = StsClient(credential, logger=logger)
    try:
        # roleJrn格式: jrn:iam::OSS主账号ID:role/角色名称
        # roleSessionName: 角色名称
        assumeRoleInfo = AssumeRoleInfo(roleJrn="jrn:iam::主账号ID:role/角色名称", roleSessionName="角色名称", durationSeconds=3600)
        parameters = AssumeRoleParameters(assumeRoleInfo=assumeRoleInfo)
        request = AssumeRoleRequest(parameters)
        resp = client.send(request)
        if resp.error is not None:
            print(resp.error.code, resp.error.message)
            return
        return resp.result
    except Exception as e:
        print(e)
        # 错误处理


def putObject():
    stsToken = getToken()
    s3 = boto3.client(
        's3',
        aws_access_key_id=stsToken["credentials"]["accessKey"],
        aws_secret_access_key=stsToken["credentials"]["secretKey"],
        aws_session_token=stsToken["credentials"]["sessionToken"],
        # 下面给出一个endpoint_url的例子
        endpoint_url='http://s3.cn-north-1.jdcloud-oss.com'
    )
    # 上传文件
    s3.upload_file("hello.txt", "BUCKET", "hello.txt")


def listObjectV2():
    stsToken = getToken()
    s3 = boto3.client(
        's3',
        aws_access_key_id=stsToken["credentials"]["accessKey"],
        aws_secret_access_key=stsToken["credentials"]["secretKey"],
        aws_session_token=stsToken["credentials"]["sessionToken"],
        # 下面给出一个endpoint_url的例子
        endpoint_url='http://s3.cn-north-1.jdcloud-oss.com'
    )
    # 上传文件
    resp = s3.list_objects_v2(Bucket="", MaxKeys=1000)
    print(resp)


if __name__ == "__main__":
    listObjectV2()