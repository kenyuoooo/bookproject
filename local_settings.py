import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SECRET_KEY = 'django-insecure-gyvedjke511-c6%xlcgje$rc5$f$v(zk&uzsastcx24d%b!q+3'

#settings.pyからそのままコピー
DATABASES = {
 'default': {
 'ENGINE': 'django.db.backends.sqlite3',
 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
 }
}
DEBUG = True