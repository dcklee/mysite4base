from django.conf import settings
from aliyunstorage.backends import AliyunOssStorage
import os


#For static files, the base class does not cater for this, need to modify base class code that includes declaring explicit variables BUCKET_PREFIX and STATIC_URL
class StaticStorage(AliyunOssStorage):
    BUCKET_PREFIX = getattr(settings, 'STATIC_ROOT')
    STATIC_URL = getattr(settings, 'STATIC_URL')

    def _clean_name(self, name):
        '''help function, useful for windows' path'''
        return os.path.join(self.BUCKET_PREFIX,
                            os.path.normpath(name).replace('\\', '/'))

    def url(self, name, force=False):
        return '{0}{1}'.format(self.STATIC_URL, name)