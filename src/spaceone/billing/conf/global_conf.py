DATABASE_AUTO_CREATE_INDEX = True
DATABASE_CASE_INSENSITIVE_INDEX = False
DATABASES = {
    'default': {
        'db': 'billing',
        'host': 'localhost',
        'port': 27017,
        'username': '',
        'password': ''
    }
}

CACHES = {
    'default': {},
    'local': {
        'backend': 'spaceone.core.cache.local_cache.LocalCache',
        'max_size': 128,
        'ttl': 300
    }
}

HANDLERS = {
}

CONNECTORS = {
    'IdentityConnector': {
    },
    'PluginConnector': {
    },
    'RepositoryConnector': {
    },
    'SecretConnector': {
    },
}
