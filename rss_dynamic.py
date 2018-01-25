from flask import Flask
from flask import render_template

import feedparser

app = Flask(__name__)

RSS_FEEDS = {
            'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
            'cnn': 'http://rss.cnn.com/rss/edition.rss',
            'fox': 'http://feeds.foxnews.com/foxnews/latest',
            'iol': 'http://www.iol.co.za/cmlink/1.640'
        }


@app.route("/<publication>")
def get_news(publication="bbc"):
    print "got "+publication
    try:
        print RSS_FEEDS[publication]
        feed =  feedparser.parse(RSS_FEEDS[publication])
        print feed
        first = feed['entries'][0]
    except Exception as e:
        print e
        return """<html>
                    <body><h1> Exception</h1></body>
                    </html>
                """
    return """<html>
                    <body>
                        <h1>Headlines </h1>
                        <b>{0}</b> </ br>
                        <i>{1}</i> </ br>
                        <p>{2}</p> </ br>
                    </body>
                </html>""".format(first.get("title"), first.get("published"), first.get("summary"))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)

