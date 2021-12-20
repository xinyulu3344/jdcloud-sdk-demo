from jdcloud_sdk.services.lb.client.LbClient import LbClient
from jdcloud_sdk.core.credential import Credential
from jdcloud_sdk.core.logger import Logger
from jdcloud_sdk.core.logger import ERROR
from jdcloud_sdk.core.config import Config
from jdcloud_sdk.core.const import SCHEME_HTTPS
import const


def getLbClient():
    credential = Credential(access_key=const.access_key, secret_key=const.secret_key)
    config = Config(endpoint='lb.jdcloud-api.com', scheme=SCHEME_HTTPS, timeout=10)
    client = LbClient(credential=credential, config=config, logger=Logger(ERROR))
    return client
