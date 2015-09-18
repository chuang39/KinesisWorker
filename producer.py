import json
from boto import kinesis

auth = {
    "aws_access_key_id":"AKIAJ7YDUGOXLHX2WWMQ",
    "aws_secret_access_key":"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"
}
connection = kinesis.connect_to_region('us-west-2', **auth)
print connection.list_streams()

#stream_name = u'ArchimedesTaskStream'
stream_name = u'TestStream'

test_data = [{'a': 'A', 'b': (2, 5), 'c': 8}]
for i in range(5):
    test_data[0]['c'] += 1
    test_json = json.dumps(test_data)
    response = connection.put_record(stream_name, test_json, 'partition_key')
    print response

