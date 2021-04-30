from walrus import Database  # A subclass of the redis-py Redis client.

db = Database()
stream = db.Stream('stream-a')
msgid1 = stream.add({'message': 'hello, streams'})
print(msgid1)
msgid2 = stream.add({'name': 'Akash'})
print(msgid2)
msgid3 = stream.add({'location': 'Mumbai'})
print(msgid3)

# Get messages 2 and newer:
messages = stream[msgid1:]
print("Stream of messages", messages)

list_of_stream=list(stream)
print(list_of_stream)

msgid4 = stream.xadd({'age': 23})

print(list_of_stream)


