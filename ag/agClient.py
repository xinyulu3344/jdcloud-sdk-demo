from jdcloud_sdk.services.ag.client.AgClient import AgClient
from jdcloud_sdk.core.credential import Credential
from jdcloud_sdk.core.logger import Logger
from jdcloud_sdk.core.logger import ERROR
from jdcloud_sdk.core.config import Config
from jdcloud_sdk.core.const import SCHEME_HTTPS
import os
import sys

sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))

from const import const



def getAgClient():
    credential = Credential(access_key=const.access_key, secret_key=const.secret_key)
    config = Config(endpoint='ag.jdcloud-api.com', scheme=SCHEME_HTTPS, timeout=10)
    client = AgClient(credential=credential, config=config, logger=Logger(ERROR))
    return client
