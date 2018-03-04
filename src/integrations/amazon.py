import base64
import datetime
import hashlib
import hmac
import re
import xml.etree.ElementTree as ET
from binascii import unhexlify
from urllib.parse import urlencode, quote_plus

import requests

from model.model import Product




class AmazonIntegration:
    def __init__(self):
        self.api = "http://webservices.amazon.com/onca/xml"

    @staticmethod
    def sign(key, val):
        return hmac.new(key, val.encode('utf-8'), hashlib.sha256).hexdigest()

    @staticmethod
    def get_timestamp():
        dateformat = "%Y-%m-%dT%H:%M:%S"
        return datetime.datetime.utcnow().strftime(dateformat)
        # return datetime.datetime.fromtimestamp(time.time()).strftime(dateformat)


    def get_products(self, product_name):
        params = [("AWSAccessKeyId", SubscriptionId), ("AssociateTag", AssociateTag),
                  ("Keywords", product_name), ("Operation", "ItemSearch"), ("ResponseGroup", "Images,ItemAttributes,Offers"),
                  ("SearchIndex", "All"), ("Service", "AWSECommerceService"),
                  ("Timestamp", self.get_timestamp())]
        string_to_sign = ""
        for (key, val) in params:
            string_to_sign+="{}={}&".format(quote_plus(key), quote_plus(val))
        string_to_sign = "GET\nwebservices.amazon.com\n/onca/xml\n" + string_to_sign[:-1]
        url_params = urlencode(params)
        signature = base64.b64encode(unhexlify(self.sign(str.encode(SECRECT_KEY), string_to_sign))).decode()
        url = "{}?{}&Signature={}".format(self.api, url_params, quote_plus(signature))
        response = requests.get(url)
        return self.parse_data(response.text)

    @staticmethod
    def parse_path(tree, path):
        try:
            return tree.find(path).text
        except:
            return ""

    def parse_data(self, xmldata):
        # interested_tags = {"ItemLinks", "MediumImage", "ItemAttributes"}
        # tree = ET.parse("../../resources/sample.xml")
        # f = open("../../resources/sample.xml")
        # data = f.read()
        data = re.sub(' xmlns="[^"]+"', '', xmldata, count=1)
        root = ET.fromstring(data)
        items = []
        for child in root[1]:
                if child.tag == "Item":
                    items.append(child)
        products = []
        for item in items:
            info = ["ItemLinks/ItemLink/URL", "MediumImage/URL", "ItemAttributes/Title",
             "Offers/Offer/OfferListing/Price/FormattedPrice", "Offers/Offer/OfferListing/Price/CurrencyCode"]
            info_ele = list(map(lambda e: self.parse_path(item, e), info))
            products.append(Product(info_ele[2], info_ele[1], info_ele[0], "{} {}".format(info_ele[3], info_ele[4])))
        return products





