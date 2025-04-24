# app.py
from flask import Flask, render_template, request, jsonify
from scrapers import product_scrapers
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def scrape_products(name):
    product_info = product_scrapers.get(name)
    if not product_info:
        return []

    url = product_info["url"]
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    return product_info["scraper"](soup)

@app.route("/<name>", methods=["GET", "POST"])
def main(name):
    product_name = request.args.get("product", name)
    product_data = scrape_products(product_name)
    return render_template("index.html", products=product_data, product_name=product_name)

@app.route("/api/products/<name>", methods=["GET"])
def api_products(name):
    product_name = request.args.get("product", name)
    product_data = scrape_products(product_name)
    return jsonify(product_data)

if __name__ == "__main__":
    app.run(host="127.0.0.1", debug=True)
