import redis
from time import sleep
r = redis.Redis(host='redis-v1-slave.default.svc.cluster.local',port=6379, db=0)

while True:
    data = r.xreadgroup('group1','cons2',{'stream1':'>'},count=1,block=0)
    r.xack('stream1','group1',(data[0][1][0][0]))
    print(f"Acknowledged frame no: {list(data[0][1][0][1].values())[0].decode('utf-8')}")
