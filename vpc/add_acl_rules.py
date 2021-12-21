from jdcloud_sdk.services.vpc.apis.AddNetworkAclRulesRequest import AddNetworkAclRulesParameters, \
    AddNetworkAclRulesRequest
from jdcloud_sdk.services.vpc.models.AddNetworkAclRuleSpec import AddNetworkAclRuleSpec
from vpcClient import *


def addNetworkAclRule():
    client = getVpcClient()
    try:
        rule = AddNetworkAclRuleSpec("TCP", "ingress", "0.0.0.0/0", "allow", 100, 1, 65535)
        parameter = AddNetworkAclRulesParameters("cn-north-1", "acl-st2zw7stic", [rule])
        request = AddNetworkAclRulesRequest(parameter)
        resp = client.send(request)
        print(resp.request_id)
        if resp.error is not None:
            print(resp.error.code, resp.error.message)
            return
        print(resp.result)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    addNetworkAclRule()
