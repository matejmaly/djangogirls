print('Ahoj!')

# b7b692aff0edf34bb881cb7c8d053a3f6d79433a

import requests
username = 'matejmaly'
token = 'b7b692aff0edf34bb881cb7c8d053a3f6d79433a'

response = requests.get(
    'https://www.pythonanywhere.com/api/v0/user/{username}/cpu/'.format(
        username=username
    ),
    headers={'Authorization': 'Token {token}'.format(token=token)}
)
if response.status_code == 200:
    print('CPU quota info:')
    print(response.content)
else:
    print('Got unexpected status code {}: {!r}'.format(response.status_code, response.content))
