import boto3


#Add and Upload list of objects on dynaomodb by serializing it
def add_list_attribute(list_objects):
       serializer = boto3.dynamodb.types.TypeSerializer()
       serialized_objects = serializer.serialize(list_objects)
       response = session.update_item(
              TableName='table_name',
              Key={
                     'id': {'S': ID},
              },
              ##to append the list with new data using another expression i.e.
              ## 'set  linked_objects = list_append(linked_objects, :list_data)'
              UpdateExpression='set  linked_objects = :list_data',
              ExpressionAttributeValues={
                     ':list_data': serialized_objects
              },
              ReturnValues="UPDATED_NEW"
       )
