from flask import Flask
import feedparser

app = Flask(__name__)

RSS_FEEDS = {
            'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
            'cnn': 'http://rss.cnn.com/rss/edition.rss',
            'fox': 'http://feeds.foxnews.com/foxnews/latest',
            'iol': 'http://www.iol.co.za/cmlink/1.640'
        }


@app.route("/bbc")
def get_bbc():
    return get_news('bbc')

@app.route('/cnn')
def get_cnn():
    return get_news('cnn')


@app.route('/fox')
def get_fox():
    return get_news('fox')

@app.route('/iol')
def get_iol():
    return get_news('iol')


def get_news(agency):
    feed =  feedparser.parse(RSS_FEEDS[agency])
    first = feed['entries'][0]
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

