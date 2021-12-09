from os import environ
from flask import Flask
import tweepy

bearer_token = environ.get("TWITTER_BEARER_TOKEN")

twitter = tweepy.Client(bearer_token=bearer_token)

app = Flask(__name__)

@app.route("/nab-tweet/<tweet_id>")
def nab_tweet(tweet_id):
    tweet = twitter.get_tweet(tweet_id, expansions="attachments.media_keys", media_fields=["type", "url"], tweet_fields=["text", "author_id"])
    user = twitter.get_user(id=tweet.data.author_id)
    urls = [media.url + ':orig' for media in tweet.includes['media']]
    print(dir(user))
    response = {
        "username": user.data.username,
        "text": tweet.data.text,
        "type": tweet.includes["media"][0].type,
        "media": urls
    }
    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0")
