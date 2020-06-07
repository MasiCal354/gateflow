import json

def construct_uri(dialect, driver='', username='', password='',
                  host='', port='', db_name='', additional_string=''):
    if driver:
        dialect += '+'
    if password:
        username += ':'
    if host:
        password += '@'
    if port:
        host += ':'
    return '%s%s://%s%s%s%s/%s%s' % (dialect,
                                     driver,
                                     username,
                                     password,
                                     host,
                                     port,
                                     db_name,
                                     additional_string)
def read_json(path):
    with open(path, 'r') as f:
        json_object = json.load(f)
    
    return json_object