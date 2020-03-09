import boto3

#Upload list of objects on dynaomodb by serializing it

serializer = boto3.dynamodb.types.TypeSerializer()
serialized_objects = serializer.serialize(list_objects)

response = session.update_item(
        TableName='table_name',
        Key={
            'id': {'S': ID},
        },
        UpdateExpression='set  linked_objects = :list_data',
        ExpressionAttributeValues={
            ':list_data': serialized_objects
        },
        ReturnValues="UPDATED_NEW"
    )
