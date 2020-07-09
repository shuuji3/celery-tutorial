broker = 'pyamqp://'
result_backend='rpc://'

task_serializer = 'json'
result_serializer = 'json'

task_annotations = {
    'tasks.add': {'rate_limit': '6/m'},
}
