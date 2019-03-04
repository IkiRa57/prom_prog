from random import randint
from time import sleep

import os

import pika


def main():
	sleep(1)
	credentials = pika.PlainCredentials('guest', 'guest')
	connection = pika.BlockingConnection(
		pika.ConnectionParameters('rabbitmq',
                                   5672,
                                   '/',
                                   credentials)
	)
	channel = connection.channel()
	channel.queue_declare(queue='hw1')

	def callback(ch, method, properties, body):
		print(int(body))

	channel.basic_consume(
		callback,
		queue='hw1',
		no_ack=True
	)
	channel.start_consuming()


if __name__ == '__main__':
	main()