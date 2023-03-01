# Importing required modules
import requests
import random
import tweepy

# Setting up Twitter API credentials
consumer_key = "YOUR_CONSUMER_KEY"
consumer_secret = "YOUR_CONSUMER_SECRET"
access_token = "YOUR_ACCESS_TOKEN"
access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"

# Creating a tweepy API object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Setting up Amazon Affiliate ID
affiliate_id = "YOUR_AFFILIATE_ID"

# Defining a list of Amazon product categories
categories = ["Books", "Electronics", "Clothing", "Toys", "Home"]

# Choosing a random category
category = random.choice(categories)

# Constructing an Amazon search URL with the category and a random page number
base_url = "https://www.amazon.com/s?k="
page_num = random.randint(1, 10)
search_url = base_url + category + "&page=" + str(page_num)

# Sending a GET request to the search URL and getting the HTML content
response = requests.get(search_url)
html_content = response.text

# Parsing the HTML content using SelectorLib (https://github.com/scrapehero/selectorlib) 
# and extracting the product details using a YAML file (amazon_products.yml) 
extractor = selectorlib.Extractor.from_yaml_file("amazon_products.yml")
products_data = extractor.extract(html_content)["products"]

# Choosing a random product from the extracted data
product_data = random.choice(products_data)

# Getting the product title, image URL and link URL from the product data
product_title = product_data["title"]
product_image_url = product_data["image"]
product_link_url = product_data["url"]

# Appending the affiliate ID to the link URL
product_link_url += "?tag=" + affiliate_id

# Posting a tweet with the product details using tweepy API object
api.update_with_media(product_image_url, status=product_title + "\n" + product_link_url)
