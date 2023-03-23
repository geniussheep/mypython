#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re

mavennodejs = "spec:\r\n  affinity:\r\n    nodeAffinity:\r\n      preferredDuringSchedulingIgnoredDuringExecution:\r\n      - weight: 1\r\n        preference:\r\n          matchExpressions:\r\n           - key: node-role.benlai.cloud/build\r\n             operator: In\r\n             values:\r\n             - jenkins-agent\r\n  tolerations:\r\n  - key: \"node-role.kubernetes.io/master\"\r\n    effect: \"NoSchedule\"\r\n  - key: \"CriticalAddonsOnly\"\r\n    operator: \"Exists\"\r\n  containers:\r\n  - name: \"nodejs\"\r\n    resources:\r\n      requests:\r\n        ephemeral-storage: \"1Gi\"\r\n      limits:\r\n        ephemeral-storage: \"10Gi\"\r\n  securityContext:\r\n    fsGroup: 1000\r\n  hostAliases:\r\n  - ip: 10.154.154.94\r\n    hostnames:\r\n    - nuget.benlailife.com\r\n  - ip: 10.154.235.133\r\n    hostnames:\r\n    - nexus.ibenlai.com\r\n"

print(mavennodejs)