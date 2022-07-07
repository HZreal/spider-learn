
from w3lib.url import canonicalize_url


url1='http://www.example.com/query?id=111&cat=222'
url2='http://www.example.com/query?cat=222&id=111'


res = canonicalize_url(url1)
print(res)          # res == url2


