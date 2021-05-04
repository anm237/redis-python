import redis
from time import sleep
try:
	r = redis.Redis(host='redis-v1-master.default.svc.cluster.local', port=6379, db=0)
	j=0
	"""
	xadd
	stream name: Need not exist will be created on first message, but consumer groups have to be created beforehand
	message: must be key,value pairs
	specify * if you want redis to assign it's own id for the message, by default assigns unix timestamp as id
	Returns
		id of the message is returned
	"""
	while True:
		for i in range(4):
			f = r.xadd('stream1',{'frameno':j},'*')
			print(f'Pushed frame no: {j} with message id {f}')
			j+=1
		sleep(1)
