from flask import Flask, render_template
from scrape import StreamScraper

app = Flask(__name__)


@app.route('/')
def home():
    scraper= StreamScraper()
    data = scraper.scrape_data()
    n= len(data)
    return render_template('index.html',games=data,n=n)


if __name__ == "__main__":
    app.run(debug=True)
