from storages.backends.s3boto3 import S3Boto3Storage
from base.settings import PUBLIC_MEDIA_LOCATION, PRIVATE_MEDIA_LOCATION, STATIC_LOCATION


class StaticStorage(S3Boto3Storage):
    location = STATIC_LOCATION
    default_acl = 'public-read'

    def path(self, name):
        super(StaticStorage, self).path(name)

    def get_accessed_time(self, name):
        super(StaticStorage, self).get_accessed_time(name)

    def get_created_time(self, name):
        super(StaticStorage, self).get_created_time(name)


class PublicMediaStorage(S3Boto3Storage):
    location = PUBLIC_MEDIA_LOCATION
    default_acl = 'public-read'
    file_overwrite = False

    def path(self, name):
        super(PublicMediaStorage, self).path(name)

    def get_accessed_time(self, name):
        super(PublicMediaStorage, self).get_accessed_time(name)

    def get_created_time(self, name):
        super(PublicMediaStorage, self).get_created_time(name)


class PrivateMediaStorage(S3Boto3Storage):
    location = PRIVATE_MEDIA_LOCATION
    default_acl = 'private'
    file_overwrite = False
    # custom_domain = False

    def path(self, name):
        super(PrivateMediaStorage, self).path(name)

    def get_accessed_time(self, name):
        super(PrivateMediaStorage, self).get_accessed_time(name)

    def get_created_time(self, name):
        super(PrivateMediaStorage, self).get_created_time(name)
