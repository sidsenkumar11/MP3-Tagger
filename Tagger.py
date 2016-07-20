import pygn
import json

clientID = '420737233-ABB8789B14C3A2BAE6730A0EEE59B3D6'
userID = '94671866235528590-B0AC2AB3FE6629CD0B956F996F3D926A'

print('\nSearch for artist "Kings of Convenience"\n')
result = pygn.search(clientID=clientID, userID=userID, artist="Miley Cyrus")
print(result)
print(json.dumps(result, sort_keys=True, indent=4))
