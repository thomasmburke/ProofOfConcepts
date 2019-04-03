import os
import facebook

token = os.getenv(key='FACEBOOK_USER_ACCESS_TOKEN')
graph = facebook.GraphAPI(access_token=token)
# Get the active user's friends.
friends = graph.get_connections(id='me', connection_name='friends')
print(friends)
