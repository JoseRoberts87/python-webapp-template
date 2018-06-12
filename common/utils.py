from app import db


# class_attributes returns a tuple with
# the class field names
def class_attributes(obj):
    exc = ['metadata', 'query', 'query_class']
    res = [x for x in dir(obj) if x[0] != '_']
    # res = [y for y in res if y not in exc]
    res.pop(res.index('metadata'))
    res.pop(res.index('query'))
    res.pop(res.index('query_class'))

    res = tuple(res)
    return res

def write_to_db(model, obj):
    try:
        db.session.add(model(**obj))
        db.session.commit()
    except Exception as e:
        print({'err': e})

    finally:
        db.session.close()


def check_status(data):
    if data is None:
        return 404
    elif data is not None:
        return 200
    else:
        return 305

def val_request(model, json_data, att):
    if json_data == None or not json_data:
        return [{'msg': 'No JSON data provided'}, 400]

    elif sorted(tuple(k for k in json_data)) != sorted(class_attributes(model)) :
        return [{'msg': 'malformed JSON object provided'}, 403]

    elif find(model, att):
        return [{'msg': 'Part Number Exists'}, 302]

    else:
        return [json_data, 200]

# this function receives a Model object and
# a JSON key value pair, returns data from DB
def find(model, data):
    # print(model.query.filter_by(**data).first())
    return model.query.filter_by(**data).first()

# this function receives a Model object
# and an ID value, returns data from DB
def find_by_id(model, id):
    print(model.query.get(id))

