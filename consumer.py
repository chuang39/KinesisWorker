import json
import time
from boto import kinesis

auth = {
    "aws_access_key_id":"AKIAJ7YDUGOXLHX2WWMQ",
    "aws_secret_access_key":"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"
}
connection = kinesis.connect_to_region('us-west-2', **auth)
print connection.list_streams()

#stream_name = u'ArchimedesTaskStream'
stream_name = u'TestStream'

"""
tries = 0
while tries < 10:
    tries += 1
    time.sleep(1)
    try:
        response = connection.describe_stream(stream_name)   
        if response['StreamDescription']['StreamStatus'] == 'ACTIVE':
            break 
    except :
        logger.error('error while trying to describe kinesis stream : %s')
else:
    raise TimeoutError('Stream is still not active, aborting...')

shard_ids = []
stream_name = None 
if response and 'StreamDescription' in response:
    stream_name = response['StreamDescription']['StreamName']                
    
    import pdb; pdb.set_trace()   
    for shard_id in response['StreamDescription']['Shards']:
        shard_id = shard_id['ShardId']
        shard_iterator_type = 'LATEST'
        shard_iterator = connection.get_shard_iterator(stream_name, shard_id, shard_iterator_type)
        shard_ids.append({'shard_id' : shard_id ,'shard_iterator' : shard_iterator['ShardIterator'] })

print shard_ids
"""

shard_id = 'shardId-000000000000'
shard_it = connection.get_shard_iterator(stream_name, shard_id, "TRIM_HORIZON")["ShardIterator"]
#shard_it = connection.get_shard_iterator(stream_name, shard_id, "AT_SEQUENCE_NUMBER", '49554167886324008940825823564806824710766500287952715778')["ShardIterator"]
while True:
    response = connection.get_records(shard_it, limit=2)
    print response
    shart_it = response["NextShardIterator"]
    time.sleep(5)


"""
tries = 0
result = []
while tries < 100:
     tries += 1
     response = connection.get_records(shard_iterator=shard_it)
     shard_iterator = response['NextShardIterator']
     if len(response['Records'])> 0:
          for res in response['Records']: 
               result.append(res['Data'])                  
          print "Result: ", result
""" 
