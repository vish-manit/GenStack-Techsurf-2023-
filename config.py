class Config(object):
    DEBUG = True
    TESTING = False

class DevelopmentConfig(Config):
    SECRET_KEY = "this-is-a-super-secret-key"

config = {
    'development': DevelopmentConfig,
    'testing': DevelopmentConfig,
    'production': DevelopmentConfig
}

## Enter your Open API Key here
OPENAI_API_KEY = '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'
PINECONE_API_KEY = 'cd1506a2-8f6b-4235-8416-7f5285fb50eb'
