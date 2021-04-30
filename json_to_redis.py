import redis
import json
import logging

'''
docker run -d -p 6379:6379 --name redis-rejson redislabs/rejson:latest

'''

r = redis.StrictRedis(host='localhost', port=6379, db=0)

def write_json_redis(arr, json_file): 
    r.execute_command('JSON.SET', arr, '.', json_file)
    

def read_from_redis_json():
    reply = json.loads((r.execute_command('JSON.GET', 'doc')).decode('utf-8'))

    user1_age=reply['user1']['age']
    print(user1_age)

    user1_car_2=reply['user1']['cars']['car2']
    print(user1_car_2)

    user2_location_1=reply['user2']['location'][0]
    print(user2_location_1)

def update_json_to_redis():
    reply = json.loads((r.execute_command('JSON.GET', 'doc')).decode('utf-8'))
    reply['user1']['cars']['car2']='Honda'
    updated_dict_to_json=json.dumps(reply)
    r.execute_command('JSON.SET', 'doc', '.', updated_dict_to_json)
    read_from_redis_json()

def write_json_array():
    sample_array='[ true, { "answer": 42 }, null ]'
    write_json_redis('arr',sample_array)
    reply = json.loads((r.execute_command('JSON.GET', 'arr')).decode('utf-8'))
    print(reply)
    list_answer=reply[1]['answer']
    print(list_answer)
    



if __name__=='__main__':

    with open('nested_sample.json','r') as f:
        json_file=f.read()
        
    write_json_redis('doc', json_file)

    read_from_redis_json()

    update_json_to_redis()

    write_json_array()




