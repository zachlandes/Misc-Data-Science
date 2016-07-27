from scrapy import Item, Field

class RedditItem(Item):
    subreddit = Field()
    link = Field()
    title = Field()
    authors = Field()
    date = Field()
    vote = Field()
    #top_comment = Field()