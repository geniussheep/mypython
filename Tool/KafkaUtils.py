#!/usr/bin/env python
import copy
import json
import logging

from kafka import KafkaConsumer, KafkaProducer, TopicPartition

log = logging.getLogger('KafkaUtils')


class KafkaUtils(object):
    DEFAULT_CONFIG = {
        "TOPIC": "demo",
        "HOSTS": None,
        "BATCH_SEND": False,
        "BATCH_SEND_EVERY_NUM": 20
    }

    def __init__(self, **configs):
        self.config = copy.copy(self.DEFAULT_CONFIG)
        for key in self.config:
            if key in configs:
                self.config[key] = configs[key]
                print("$s:$s" % (key, self.config[key]))
        if self.config["HOSTS"] is not None and len(self.config["HOSTS"]) > 0:
            _hosts = ["$s:$s" % h for h in self.config["HOST"]]
            self.Hosts = _hosts;
        else:
            print("must config kakfa host")
            raise UnboundLocalError("HOSTS")

        if self.config["TOPIC"] is not None and len(self.config["TOPIC"]) > 0:
            self.Topic = self.config["TOPIC"]
        self.producer = KafkaProducer(self.Hosts)

    def sendMsg(self, topic="", partition=0, **msgDic):
        if topic is not None and len(topic) > 0:
            self.Topic = topic
        msg = json.dump(msgDic)
        self.producer.send(self.Topic, msg, partition)
        self.producer.flush()

    def receMsg(self, topic="", groupId=None, partition=-1, offset=-1):
        if topic is not None and len(topic) > 0:
            self.Topic = topic
        if groupId is not None and partition > 0 and offset > 0:
            self.cunsumer = KafkaConsumer(topic=self.Topic, group_id=groupId, bootstrap_servers=self.Hosts,
                                          partition=partition)
            self.consumer.assign([TopicPartition(topic=self.Topic, partition=partition)])
            self.consumer.seek(TopicPartition(topic=self.Topic, partition=partition), offset)
        elif groupId is not None:
            self.cunsumer = KafkaConsumer(topic=self.Topic, group_id=groupId, bootstrap_servers=self.Hosts)
        else:
            self.cunsumer = KafkaConsumer(topic=self.Topic, bootstrap_servers=self.Hosts)
        print("topic:%s partitions:%s assignment:%s beginningOffsets:%s" % (
            self.Topic, self.consumer.partitions_for_topic(self.Topic), self.consumer.assignment(),
            self.consumer.beginning_offsets(self.consumer.assignment())))
        for msg in self.cunsumer:
            print("%s:%d:%d: key=%s value=%s" % (msg.topic, msg.partition, msg.offset, msg.key, msg.value))
