"""
Przy użyciu biblioteki requests, napisz prosty program,
który połączy się z dowolną stroną i ściągnie HTML strony głównej.

Podpowiedź: zajrzyj do http://docs.python-requests.org/en/master/
"""

import requests
r = requests.get('http://badcompany.com.pl/')


#print(r.text)
print(r.headers['content-type'])
print(r.status_code) # 200

# # 'application/json; charset=utf8'
# r.encoding
# # 'utf-8'
# r.text
# u'{"type":"User"...'
# r.json()
# {u'private_gists': 419, u'total_private_repos': 77, ...}



# response = requests.get('http://coderslab.pl')
# print(response.text)
