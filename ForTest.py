#!/usr/bin/env python3
# -*- coding: utf-8 -*-

str = "5072 Benlai.WMS.Logistics.OpenAPI|5005 Benlai.WMS.DO.ESBPublishService|4930 Benlai.WMS.Delivery.APIHost|3910 Benlai.WMS.DeliveryServer.WebAPI|3911 Benlai.WMS.Delivery.ESBConsume|5098 Benlai.WMS.Transportation.ServiceHost|1852 Benlai.WMS.DO.ESB.Consume|1861 Benlai.WMS.DO.WebApi|1823 Benlai.WMS.Logistics.ServiceHosts|1833 Benlai.WMS.Delivery.WebApi|1845 Benlai.WMS.Delivery.ScheduleTask|5104 Benlai.WMS.Transportation.ScheduleTask|5132 Benlai.WMS.Delivery.Basic.ServiceHost|6188 Benlai.WMS.Transportation.ESBConsume|8193 Benlai.WMS.Delivery.Basic.Task"
arr = str.split("|")
print(arr)
result = [int(x.split(" ")[0]) for x in arr]
result.sort()
for x in result:
    print("%d" % x)
resultstr = " ".join(map(str, [int(x.split(" ")[0]) for x in arr]))
print("%s" % resultstr)

