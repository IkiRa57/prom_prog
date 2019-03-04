from random import randint
from time import sleep

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

	while True:
		data = randint(0, 2**31)
		channel.basic_publish(
			exchange='',
			routing_key='hw1',
			body=str(data)	
		)
		sleep(randint(1, 5))

if __name__ == '__main__':
	main()