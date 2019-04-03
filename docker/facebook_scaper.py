import os
from s3_ops import S3Ops
import facebook
import json

token = os.getenv(key='FACEBOOK_USER_ACCESS_TOKEN')
graph = facebook.GraphAPI(access_token=token)
# Get the active user's friends.
friends = graph.get_connections(id='me', connection_name='friends')
print(type(friends))

S3Ops().stream(data=json.dumps(friends),fileName='facebook_friends.json')
