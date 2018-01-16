import twitter
from django.conf import settings


api_twitter = twitter.Api(
    consumer_key=getattr(settings, 'TW_CONSUMER_KEY'),
    consumer_secret=getattr(settings, 'TW_CONSUMER_SECRET'),
    access_token_key=getattr(settings, 'TW_ACCESS_TOKEN_KEY'),
    access_token_secret=getattr(settings, 'TW_ACCESS_TOKEN_SECRET')
)
