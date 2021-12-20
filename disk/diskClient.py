from jdcloud_sdk.core.credential import Credential
from jdcloud_sdk.services.disk.client.DiskClient import DiskClient
from jdcloud_sdk.core.logger import Logger
from jdcloud_sdk.core.logger import ERROR
from jdcloud_sdk.core.const import SCHEME_HTTPS
from jdcloud_sdk.core.config import Config
import const


def getDiskClient():
    credential = Credential(access_key=const.access_key, secret_key=const.secret_key)
    config = Config(endpoint='cdn.jdcloud-api.com', scheme=SCHEME_HTTPS, timeout=10)
    client = DiskClient(credential=credential, config=config, logger=Logger(ERROR))
    return client
