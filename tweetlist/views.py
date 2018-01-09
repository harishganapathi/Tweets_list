from django.shortcuts import render,redirect,get_object_or_404
#from .forms import Tweets
import requests
import requests_oauthlib
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect



authenticate = requests_oauthlib.OAuth1(API_kEY,API_SECRET,ACCESS_TOKEN,ACCESS_TOKEN_SECRET)
url = "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name="

def home(request):
    return render(request,'tweetlist/index.html',{})


def listweets(request):
    profileName = str(request.POST.get('profilename',None))
    count = str(request.POST.get('tweetcount',None))
    if count == "":
        count = 7
    else:
        count = str(request.POST.get('tweetcount', None))
    print('------------------------>>>>> -------debug bar <---')
    print(count)
    r = requests.get(url + profileName + "&count="+str(count), auth=authenticate)
    tweets = []
    for tweet in r.json():
        tweets.append(tweet['text'])
    print(tweets)
    return JsonResponse({'profileName': profileName, 'tweets': tweets})

