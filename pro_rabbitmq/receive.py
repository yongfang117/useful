#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 版本说明pika==0.10.0
import pika

queue = 'oss.url_test'  # 队列名
routing_key = 'url_test'
exchange = 'oss_test'

hostname = '10.6.3.14'
# hostname = '192.168.211.130'
port = 5672

credentials = pika.PlainCredentials(username='mq_user', password='password')
parameters = pika.ConnectionParameters(host=hostname, port=port, virtual_host='wolong', credentials=credentials)
connection = pika.BlockingConnection(parameters=parameters)
# 创建通道
channel = connection.channel()
channel.queue_declare(queue=queue, durable=True)


def callback(ch, method, properties, body):
    print(" [x] Received %r" % (body,))

    ch.basic_ack(delivery_tag=method.delivery_tag)  # 发送ack消息


# 添加不按顺序分配消息的参数,可有可无
# channel.basic_qos(prefetch_count=1)
# 告诉rabbitmq使用callback来接收信息
# channel.basic_consume(callback, queue=queue, no_ack=False)  # no_ack来标记是否需要发送ack，默认是False，开启状态 pika=0.10.0可以这样
channel.basic_consume(queue, callback, False)  # pika=1.1.0 位置需要这样

# 开始接收信息，并进入阻塞状态，队列里有信息才会调用callback进行处理,按ctrl+c退出
print(' [*] Waiting for messages. To exit press CTRL+C')

channel.start_consuming()