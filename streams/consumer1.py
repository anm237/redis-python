import redis
from time import sleep

r = redis.Redis(host='redis-v1-master.default.svc.cluster.local',port=6379, db=0,decode_responses=True)

"""
block (integer): blocks single read operation till new event is streamed for said milliseconds
count: number of messages to read at once, can pull more than 1 only if block is None
consumer name(string): consumer name has to be unique and must be specified for xreadgroup
group name(string): similar to multiple subscriptions we use in pubsub, {input-topic-->{od_group,pe_group}}, useful to deliver same message to different functional components

Returns:
    If block!=None:
        Returns a List eg. [b'topic_name',[(b'message_id', {b'key': b'value',...})]]
    If block==None && Count > 1:
        Returns a List eg. [b'topic_name',[(b'message_id', {b'key': b'value',...}),(nextmessage),...]]
"""
while True:
    data = r.xreadgroup('group1','cons1',{'stream1':'>'},count=1,block=0)
    r.xack('stream1','group1',(data[0][1][0][0]))
    print(f"Acknowledged frame no: {list(data[0][1][0][1].values())[0].decode('utf-8')}")
