from flask import make_response
import json
def serialize(obj):
        '''Used to convert a class to json'''
        return obj.__dict__

def toJSONResponse(object):
    '''Convert an object to json response'''
    data = object.__dict__
    response = make_response(json.dumps(data, default = serialize))
    response.headers['Content-Type'] = 'application/json'
    ##print(json.dumps(data, default = serialize))
    return response