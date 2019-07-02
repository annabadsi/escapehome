from .common import *

ALLOWED_HOSTS = ['homeescape.pythonanywhere.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'homeescape$homeescape',
        'USER': 'homeescape',
        'PASSWORD': 'BzgU3t93qMQEBxdEEbTYRBv3',
        'HOST': 'homeescape.mysql.pythonanywhere-services.com',
        'PORT': '3306',
    }
}
