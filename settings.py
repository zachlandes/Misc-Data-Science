#settings.py
BOT_NAME = 'reddit'
SPIDER_MODULES = ['reddit.spiders']
NEWSPIDER_MODULE = 'reddit.spiders'

DOWNLOAD_DELAY = 2

ITEM_PIPELINES = {'reddit.pipelines.DuplicatesPipeline':300, 'reddit.pipelines.MongoDBPipeline':800, }

MONGODB_SERVER = "localhost"
MONGODB_PORT = 27017
MONGODB_DB = "reddit"
MONGODB_COLLECTION = "post" 