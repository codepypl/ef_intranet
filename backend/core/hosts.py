from django_hosts import host

host_patterns = [
    host(r'logowanie', 'apps.auth.urls', name='auth'),

]