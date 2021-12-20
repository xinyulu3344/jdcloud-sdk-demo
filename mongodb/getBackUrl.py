import unittest
from jdcloud_sdk.core.credential import Credential
from jdcloud_sdk.core.config import Config
from jdcloud_sdk.core.const import SCHEME_HTTP

from jdcloud_sdk.services.mongodb.client.MongodbClient import MongodbClient
from jdcloud_sdk.services.mongodb.apis.DescribeInstancesRequest import *
from jdcloud_sdk.services.mongodb.apis.BackupDownloadURLRequest import *
from jdcloud_sdk.core.config import Config
from jdcloud_sdk.core.const import SCHEME_HTTP
from jdcloud_sdk.services.mongodb.apis.DescribeBackupsRequest import *


def BackupDownloadURL(credential, regionId, backupId):
    config = Config(endpoint="www.jdcloud-api.com", scheme=SCHEME_HTTP)
    client = MongodbClient(credential, config)
    try:
        parameters = BackupDownloadURLParameters(regionId, backupId)
        request = BackupDownloadURLRequest(parameters, header=None, version='v1')
        resp = client.send(request)
        if resp.error is not None:
            print(resp.error.code, resp.error.message)
        print(resp)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    access_key = 'EE35CF02BF28533628A64594A8641E04'
    secret_key = '8E110D81823C9C5F1A773FCC54415DC8'
    my_regionId = 'cn-north-1'
    my_credential = Credential(access_key, secret_key)
    my_credential_2 = Credential(access_key, secret_key)
    tmp_backupId = 'mongo-0i770e9byp@016160041448646'
    BackupDownloadURL(my_credential_2, my_regionId, tmp_backupId)
