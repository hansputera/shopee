from flask import Flask, jsonify, current_app
app = Flask(__name__)
import urllib
from shopee import cariBarang, flashSales
import json


@app.route("/")
def welcomeScreeen():
	return jsonify({
		"h e l l o": "w o r l d"
	})
@app.route("/search/<product_name>")
def searchProduct(product_name):
	product = cariBarang(urllib.parse.quote(str(product_name), encoding="utf-8"))
	if product == None:
		return jsonify({
			"success": False,
			"message": "Not found"
		})

	else:
		return current_app.response_class(json.dumps(product, indent=4), mimetype="application/json")

@app.route("/flash-sales")
def flashsales():
	return current_app.response_class(json.dumps(flashSales(), indent=4), mimetype="application/json")

if __name__ == "__main__":
	app.run(
		host="0.0.0.0",
		port=3419
	)