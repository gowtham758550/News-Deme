from flask import Flask, render_template
from requests import get
from config import key

app = Flask(__name__)

@app.route('/')
def index():
	response = get("https://newsapi.org/v2/top-headlines?country=in", params = {'apiKey' : key}).json()
	return render_template('index.html', name = response)

@app.route('/sources')
def sources():
	response = get("https://newsapi.org/v2/sources", params = {'apiKey' : key}).json()
	return render_template('sources.html', name = response)

@app.route('/about')
def about():
	return render_template('about.html')
	

if __name__ == "__main__":
	app.run()
