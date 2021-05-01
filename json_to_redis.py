import redis
import json
import logging

'''
docker run -d -p 6379:6379 --name redis-rejson redislabs/rejson:latest

'''

r = redis.StrictRedis(host='localhost', port=6379, db=0)

def write_json_redis(arr, json_file): 
    """
    Write a json file to redis.

    Args:
        arr (string): Key in redis that points to the JSON
        json_file (string): JSON file read as string
    """
    r.execute_command('JSON.SET', arr, '.', json_file)
    

def read_from_redis_json():
    """
    Reading the JSON from redis as Python dictionary.
    """
    reply = json.loads((r.execute_command('JSON.GET', 'doc')).decode('utf-8'))

    user1_age=reply['user1']['age']
    print(user1_age)

    user1_car_2=reply['user1']['cars']['car2']
    print(user1_car_2)

    user2_location_1=reply['user2']['location'][0]
    print(user2_location_1)

def update_json_to_redis():
    """
    Update operation using python dictionary. Dictionary is converted back to JSON strong.
    """
    reply = json.loads((r.execute_command('JSON.GET', 'doc')).decode('utf-8'))
    reply['user1']['cars']['car2']='Honda'
    updated_dict_to_json=json.dumps(reply)
    r.execute_command('JSON.SET', 'doc', '.', updated_dict_to_json)
    read_from_redis_json()

def write_json_array():
    """
    Writing an array object to redis. It is read as Python list.
    """
    sample_array='[ true, { "answer": 42 }, null ]'
    write_json_redis('arr',sample_array)
    reply = json.loads((r.execute_command('JSON.GET', 'arr')).decode('utf-8'))
    print(reply)
    list_answer=reply[1]['answer']
    print(list_answer)
    



if __name__=='__main__':
    #Opening and reading a local file
    with open('nested_sample.json','r') as f:
        json_file=f.read()
    
    #Function call to write to redis   
    write_json_redis('doc', json_file)

    #Function call read sample fields from redis
    read_from_redis_json()

    #Fucntion call to update sample fields in redis
    update_json_to_redis()

    #Function call to write an array to redis
    write_json_array()




