from functools import wraps, lru_cache

import urllib.request
import time

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
    time.sleep(3)
    return urllib.request.urlopen(url).read()

@lru_cache(maxsize=None)
def web_lookup2(url):
    time.sleep(3)
    return urllib.request.urlopen(url).read()

print("Custom decorator:")
print(web_lookup('http://example.com'))
print('\n')
print(web_lookup('http://example.com'))

print('\n' * 2)

print('Built-in lru_cache decorator:')
print(web_lookup2('http://example.com'))
print('\n')
print(web_lookup2('http://example.com'))
