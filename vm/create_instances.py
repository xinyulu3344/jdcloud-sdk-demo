from jdcloud_sdk.services.vm.apis.CreateInstancesRequest import CreateInstancesParameters, CreateInstancesRequest
from jdcloud_sdk.services.vm.models.InstanceSpec import InstanceSpec
from jdcloud_sdk.services.vm.models.InstanceNetworkInterfaceAttachmentSpec import InstanceNetworkInterfaceAttachmentSpec
from jdcloud_sdk.services.vm.models.InstanceDiskAttachmentSpec import InstanceDiskAttachmentSpec
from jdcloud_sdk.services.disk.models.DiskSpec import DiskSpec
from jdcloud_sdk.services.vpc.models.NetworkInterfaceSpec import NetworkInterfaceSpec
from jdcloud_sdk.services.vpc.models.ElasticIpSpec import ElasticIpSpec
from jdcloud_sdk.services.charge.models.ChargeSpec import ChargeSpec
from vmClient import *


def createInstances01():
    client = getVmClient()

    # 网络配置
    networkInterface = NetworkInterfaceSpec(az=None, subnetId="subnet-l0zdpycema", primaryIpAddress=None)
    network = InstanceNetworkInterfaceAttachmentSpec(networkInterface=networkInterface)

    # 系统盘配置
    sysDiskSpec = DiskSpec(az="cn-north-1c", name="sdktest", diskType="hdd.std1", diskSizeGB=100)
    sysDisk = InstanceDiskAttachmentSpec(diskCategory='cloud', cloudDiskSpec=sysDiskSpec)

    # 数据盘配置
    dataDiskSpec = DiskSpec(az='cn-north-1c', name='sdktest', diskType='hdd.std1', diskSizeGB=100)
    dataDisk = InstanceDiskAttachmentSpec(diskCategory='cloud', cloudDiskSpec=dataDiskSpec,
                                          deviceName='vdb', autoDelete=False)
    dataDisks = list()
    dataDisks.append(dataDisk)

    # 公网ip配置
    elasticIp = ElasticIpSpec(1, "bgp")

    # 计费
    # charge = ChargeSpec(chargeMode="prepaid_by_duration", chargeUnit="month", chargeDuration=1)
    charge = ChargeSpec(chargeMode="postpaid_by_duration")

    instanceSpec = InstanceSpec(az="cn-north-1c", instanceType="g.n2.medium", name='sdktest',
                                imageId="img-nz0hp1xv1x", primaryNetworkInterface=network,
                                systemDisk=sysDisk, dataDisks=dataDisks, keyNames=None, description='vmsdktest',
                                charge=charge, agId=None, elasticIp=elasticIp)

    try:
        parameters = CreateInstancesParameters("cn-north-1", instanceSpec)
        parameters.setMaxCount(1)
        request = CreateInstancesRequest(parameters)
        resp = client.send(request)
        print(resp.request_id)
        if resp.error is not None:
            print(resp.error.code, resp.error.message)
            return
        result = resp.result
        print("创建云主机：", result)
    except Exception as e:
        print(e)


def createInstances02():
    client = getVmClient()
    instanceSpec = {
        "az": "cn-north-1b",
        "name": "arp_test",
        "imageId": "img-nz0hp1xv1x",
        "instanceType": "g.n2.medium",
        "password": "",
        "systemDisk": {
            "diskCategory": "cloud",
            "cloudDiskSpec": {
                "diskType": "hdd.std1",
                "diskSizeGB": 40
            }
        },
        "primaryNetworkInterface": {
            "networkInterface": {
                "subnetId": "subnet-l0zdpycema",
                "primaryIpAddress": "192.168.2.170",
            }
        }
    }
    try:
        parameters = CreateInstancesParameters(regionId="cn-north-1", instanceSpec=instanceSpec)
        request = CreateInstancesRequest(parameters)
        resp = client.send(request)
        print(resp.request_id)
        if resp.error is not None:
            print(resp.error.code, resp.error.message)
            return
        print(resp.result)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    # createInstances01()
    createInstances02()
