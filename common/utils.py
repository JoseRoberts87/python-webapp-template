
def class_attributes(obj):
    exc = ['metadata', 'query', 'query_class']
    res = [x for x in dir(obj) if x[0] != '_']
    # res = [y for y in res if y not in exc]
    res.pop(res.index('metadata'))
    res.pop(res.index('query'))
    res.pop(res.index('query_class'))

    res = tuple(res)
    return res