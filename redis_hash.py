import redis
import json
import logging

r = redis.StrictRedis(host='localhost', port=6379, db=0)

'''
Sample JSON file used:

{"name": "John", "age": "31", "city": "New York"}

'''
def write_to_redis(json_file):
  redis_data=json_file
  redis_data_dict=json.loads(redis_data) 
  r.hmset('sample1',redis_data_dict)

def read_from_redis(list1):
  redis_keys= r.keys()
  print(redis_keys)
  value=r.hmget('sample1',list1[0],list1[1])
  print(value) #list

def update_to_redis(dict1):
  r.hmset('sample1', dict1)
  value=r.hmget('sample1','country')
  print(value)

def delete_from_redis(delete_key):
  r.delete('sample1', delete_key)
  print(r.hmget('sample1', delete_key))

def delete_hash_from_redis(delete_hash):
  r.delete(delete_hash)
  print(r.hmget(delete_hash,'name'))

if __name__ == '__main__':
  
  with open('sample.json','r') as f:
    json_file=f.read()
  write_to_redis(json_file)

  list1=['name','age']
  read_from_redis(list1)

  dict1={'country':'India'}
  update_to_redis(dict1)

  delete_key='country'
  delete_from_redis(delete_key)
 
  delete_hash='sample1'
  delete_hash_from_redis(delete_hash)


