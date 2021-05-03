import redis
from time import sleep
r = redis.Redis(host='redis-v1-master.default.svc.cluster.local', port=6379, db=0)
r.xgroup_create('stream1','group1','$')
print('Group created')
