from flask import Flask
from flask import render_template
from flask import request
import feedparser

app = Flask(__name__)

RSS_FEEDS = {
            'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
            'cnn': 'http://rss.cnn.com/rss/edition.rss',
            'fox': 'http://feeds.foxnews.com/foxnews/latest',
            'iol': 'http://www.iol.co.za/cmlink/1.640'
        }
@app.route("/")
def get_news():
    query = request.args.get("publication")
    print query
    if not query or query.lower() not in RSS_FEEDS:
        publication = "bbc"
    else:
        publication = query.lower()

    feed = feedparser.parse(RSS_FEEDS[publication])
    return render_template("get.html",articles=feed['entries'])
if __name__  == '__main__':
    app.run(host="0.0.0.0",port=5000, debug=True)
