import boto3
import json

client = boto3.Session(region_name='eu-west-1').client('dynamodb')
boto3.resource('dynamodb')

your_id = 'project-id'

##query by global secondary index i.e. project_id-index
updateStatus = client.query(
    TableName='Testing',
    IndexName='project_id-index',
    KeyConditionExpression="  #G = :project_id",
    ExpressionAttributeNames={"#G": "project_id"},
    ExpressionAttributeValues={
        ":project_id": {"S": your_id}
    }
)
##to get primary key i.e. ID to update the table by adding attribute
test = updateStatus['Items'][0]
deserializer = boto3.dynamodb.types.TypeDeserializer()
python_data = {k: deserializer.deserialize(
    v) for k, v in test.items()}
python_data = python_data['project_id']


response = client.update_item(
    TableName='Testing',
    Key={
        'project_id': {'S': python_data},
    },
    UpdateExpression="set test1 = :t1, test2=:t2",
    ExpressionAttributeValues={
        ':t1': {'S': 'abcd1'},
        ':t2': {'S': "My text"}
    },
    ReturnValues="UPDATED_NEW"

)

print(json.dumps(response, indent=4))
