import redis
import json
import logging

r = redis.StrictRedis(host='localhost', port=6379, db=0)

'''
Sample JSON file used:

{"name": "John", "age": "31", "city": "New York"}

'''
def write_to_redis(json_file):
  """
  Write a JSON file to redis hash. Data is uploaded as Python dictionary

  Args:
      json_file (string): JSON file read as string
  """
  redis_data=json_file
  redis_data_dict=json.loads(redis_data) 
  r.hmset('sample1',redis_data_dict)

def read_from_redis(list1):
  """
  Read sample values with keys passed as Python list

  Args:
      list1 (list): List of sample keys to retrieve corresponding values
  """
  redis_keys= r.keys()
  print(redis_keys)
  value=r.hmget('sample1',list1[0],list1[1])
  print(value) #list

def update_to_redis(dict1):
  """
  Update sample fields to redis hash. Once updated read that field.

  Args:
      dict1 (dictionary): A new dictionary to be updated in redis hash
  """
  r.hmset('sample1', dict1)
  value=r.hmget('sample1','country')
  print(value)

def delete_from_redis(delete_key):
  """
  Delete a particular key in redis hash

  Args:
      delete_key (string): Key to be deleled from the redis hash
  """
  r.delete('sample1', delete_key)
  print(r.hmget('sample1', delete_key))

def delete_hash_from_redis(delete_hash):
  """
  Delete the entire hash object from redis

  Args:
      delete_hash (string): Name of the hash to be deleted
  """
  r.delete(delete_hash)
  print(r.hmget(delete_hash,'name'))

if __name__ == '__main__':
  
  #Open and read a local json file
  with open('sample.json','r') as f:
    json_file=f.read()

  #Function call to write the file to redis hash
  write_to_redis(json_file)

  #Function to call read values of sample list of keys
  list1=['name','age']
  read_from_redis(list1)
 
  #Function call to update a redis hash with sample dictionary
  dict1={'country':'India'}
  update_to_redis(dict1)

  #Function call to delete a key in redis hash
  delete_key='country'
  delete_from_redis(delete_key)
 
  #Function call to delete entire hash in redis
  delete_hash='sample1'
  delete_hash_from_redis(delete_hash)


