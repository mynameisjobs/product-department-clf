import sys

import requests

resp = requests.get('http://localhost:8000/predict', params={
    'title': '%s'%(sys.argv[1])
    })
print(resp.text)
