from django.shortcuts import render
import tweepy
from tweepy.auth import OAuthHandler

# Create your views here.
def home_timeline(request):
    auth = OAuthHandler('uUzwHoGkLAfBnh7ikTlFCfJGY', 'dxJC3GhITojO5yvQKSNfwjhz6qy1lhfWQVIbQJFhkt2BGpWKXj')
    auth.set_access_token('74882407-I2j0uWpvc2yOSOmcwUkrKVZIxQeQACzHd7LUDt80S', 'Q2D1ndAaDxp9Z13r0PazUz5IDU5BvotW1qYCG2ES3izSo')

    api = tweepy.API(auth)

    public_tweets = api.home_timeline()

    return render(request, 'public_tweets.html', {'public_tweets': public_tweets})