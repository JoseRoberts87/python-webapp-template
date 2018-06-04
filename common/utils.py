from app import db

def class_attributes(obj):
    exc = ['metadata', 'query', 'query_class']
    res = [x for x in dir(obj) if x[0] != '_']
    # res = [y for y in res if y not in exc]
    res.pop(res.index('metadata'))
    res.pop(res.index('query'))
    res.pop(res.index('query_class'))

    res = tuple(res)
    return res

def write_to_db(obj):
    db.session.add(obj)
    db.session.commit()


def check_status(data):
    if data is None:
        return 404
    elif data is not None:
        return 200
    else:
        return 305

def test_data(json_data, att):
    if json_data == None or not json_data:
        return [{'msg': 'No data found'}, 400]

    elif json_data[att] in list(['kiva1']):
        return [{'msg': 'Part Number Exists'}, 302]

    else:
        return json_data

# this function receives a Model object and
# a JSON key value pair, returns data from DB
def find(model, data):
    print(model.query.filter_by(**data).first())
    return model.query.filter_by(**data).first()

# this function receives a Model object
# and an ID value, returns data from DB
def find_by_id(model, id):
    print(model.query.get(id))

