import urllib.request

def web_lookup(url, saved={}):
    if url in saved:
        return saved[url]
    page = urllib.request.urlopen(url).read()
    saved[url] = page
    return page

cache = {}
print(web_lookup('http://example.com'), cache)
print('\n')
print(web_lookup('http://example.com'), cache)
