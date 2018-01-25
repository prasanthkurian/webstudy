from flask import Flask
from flask import render_template

import feedparser

RSS_FEEDS = {
            'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
            'cnn': 'http://rss.cnn.com/rss/edition.rss',
            'fox': 'http://feeds.foxnews.com/foxnews/latest',
            'iol': 'http://www.iol.co.za/cmlink/1.640'
        }

app = Flask(__name__) 

@app.route("/<publication>")
def get_news(publication="bbc"):
    try:
        feed = feedparser.parse(RSS_FEEDS[publication])
        first = feed['entries'][0]
    except Exception as e:
        print e
        return "<html></html>"
    return render_template("home.html", articles=feed['entries'])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)