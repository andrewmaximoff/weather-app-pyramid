from pyramid.view import view_config

from .weather import query_api

CITY_NAME = [
    {'name': 'Toronto'}, {'name': 'Montreal'}, {'name': 'Calgary'},
    {'name': 'Ottawa'}, {'name': 'Edmonton'}, {'name': 'Mississauga'},
    {'name': 'Winnipeg'}, {'name': 'Vancouver'}, {'name': 'Brampton'},
    {'name': 'Quebec'}, {'name': 'Konotop'}, {'name': 'Kiev'},
]


@view_config(route_name='index', renderer='templates/weather.jinja2')
def index(request):
    return {'cities': CITY_NAME}


@view_config(route_name='result', renderer='templates/result.jinja2')
def result(request):
    data = []
    error = None
    select = request.params['comp_select']
    resp = query_api(select)
    if resp:
        data.append(resp)
    if len(data) != 2:
        error = 'Bad Response from Weather API'
    return {'data': data, 'error': error}
