from functools import wraps

import urllib.request

def cache(func):
    saved = {}
    @wraps(func)
    def newfunc(*args):
        if args in saved:
            return saved[args]
        result = func(*args)
        saved[args] = result
        return result
    return newfunc

@cache
def web_lookup(url):
    return urllib.request.urlopen(url).read()

print(web_lookup('http://example.com'))
print('\n')
print(web_lookup('http://example.com'))
