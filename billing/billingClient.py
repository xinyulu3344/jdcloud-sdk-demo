from jdcloud_sdk.core.credential import Credential
from jdcloud_sdk.services.billing.client.BillingClient import BillingClient
from jdcloud_sdk.core.logger import Logger
from jdcloud_sdk.core.logger import ERROR
from jdcloud_sdk.core.config import Config
from jdcloud_sdk.core.const import SCHEME_HTTPS
import os
import sys

sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
from const import const


def getBillingClient():
    credential = Credential(const.access_key, const.secret_key)
    config = Config(endpoint="billing.jdcloud-api.com", scheme=SCHEME_HTTPS)
    client = BillingClient(credential, config=config, logger=Logger(ERROR))
    return client
