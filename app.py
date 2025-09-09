from flask import Flask, jsonify
import requests
from lxml import html

app = Flask(__name__)

@app.route("/scrape", methods=["GET"])
def scrape():
    url = "https://igold.ae/gold-rate"
    response = requests.get(url)
    response.raise_for_status()

    tree = html.fromstring(response.content)
    element = tree.xpath('//*[@id="aed"]/div[1]/div[2]')

    if element:
        data = element[0].text_content().strip()
        return jsonify({"data": data})
    else:
        return jsonify({"error": "Element not found"}), 404

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=1000)
