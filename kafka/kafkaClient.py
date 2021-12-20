from jdcloud_sdk.services.kafka.client.KafkaClient import KafkaClient
from jdcloud_sdk.core.credential import Credential
from jdcloud_sdk.core.logger import Logger
from jdcloud_sdk.core.logger import ERROR
from jdcloud_sdk.core.config import Config
from jdcloud_sdk.core.const import SCHEME_HTTPS
import const


def getKafkaClient():
    credential = Credential(access_key=const.access_key, secret_key=const.secret_key)
    config = Config(endpoint='kafka.jdcloud-api.com', scheme=SCHEME_HTTPS, timeout=10)
    client = KafkaClient(credential=credential, config=config, logger=Logger(ERROR))
    return client
