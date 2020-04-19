def construct_uri(dialect, driver='', username='', password='', host='', port='', db_name='', additional_string=''):
    if driver:
        dialect += '+'
    if password:
        username += ':'
    if host:
        password += '@'
    if port:
        host += ':'
    return '%s%s://%s%s%s%s/%s/%s'%(dialect, driver, username, password, host, port, db_name, additional_string)