#!/bin/python3

import requests
baseURL = "https://shopee.co.id/api/v2"

def cariBarang(barang: str):
	response = requests.get(f"{baseURL}/search_items?by=relevance&keyword={barang}", headers={
		"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.66"
	})

	data = response.json()
	
	if data['items'] == None:
		return None
	else:
		data_ = {
			"count": len(data['items']),
			"algorithm": data['algorithm'],
			"items": []
		}

		for item in data['items']:
			item_ = {
				"id": item['itemid'],
				"brand": item['brand'],
				"priceInfo": {
					"currency": item['currency']
				},
				"itemName": item['name'].strip(),
				"liked_count": item['liked_count'],
				"location": item['shop_location'].strip(),
				"verified": item['shopee_verified'],
				"solds": item['historical_sold'],
				"stocks": item['stock'],
				"image": f"https://cf.shopee.co.id/file/{item['image']}",
				"adult": item['is_adult']
			}

			if item['discount'] == None:
				item_['priceInfo']['price'] = round(item['price'] / 100000, 0)
			else:
				item_['priceInfo']['price'] = round(item['price'] / 100000, 0)
				item_['priceInfo']['discount'] = item['discount']
				item_['priceInfo']['priceBeforeDiscount'] = round(item['price_before_discount'] / 100000, 0)
			
			data_['items'].append(item_)
		return data_

def flashSales():
	response = requests.get(f"{baseURL}/flash_sale/flash_sale_get_items")
	json = response.json()

	data_ = {
		"count": len(json['data']['items']),
		"items": []
	}

	for item in json['data']['items']:
		item_ = {
			"id": item['itemid'],
			"name": item['name'].strip(),
			"priceInfo": {
				"currency": "IDR",
				"discount": item['discount'],
				"price": item['price'] / 100000,
				"priceBeforeDiscount": item['price'] / 100000
			},
			"image": f"https://cf.shopee.co.id/file/{item['image']}",
			"shopInfo": {
				"id": item['shopid'],
				"official": item['is_shop_official'],
				"preffered": item['is_shop_preferred']
			},
			"stocks": item['stock'],
			"duraction": {
				"s": item['start_time'],
				"e": item['end_time']
			},
			"voucher": item['voucher']
		}

		# if item['voucher'] != None:
		# 	item_['voucher'] = {
		# 		"code": item['voucher']['voucher_code'],
		# 		"id": item['voucher']['promotionId'],
		# 		"spend": item['voucher']['min_spend']
		# 	}
		data_['items'].append(item_)
	return data_