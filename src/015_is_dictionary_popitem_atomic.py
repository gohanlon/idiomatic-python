d = {'matthew': 'blue', 'rachel': 'green', 'raymond': 'red'}

while d:
    key, value = d.popitem()
    print(key, '-->', value)

# Note: `dict.popitem` it is atomic, but the above presented code doesn't show that
