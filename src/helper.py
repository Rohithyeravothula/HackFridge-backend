

def get_products(self, product_name):
    params = [("AWSAccessKeyId", SubscriptionId), ("AssociateTag", AssociateTag),
              ("Keywords", product_name), ("Operation", "ItemSearch"),
              ("ResponseGroup", "Images,ItemAttributes,Offers"),
              ("SearchIndex", "All"), ("Service", "AWSECommerceService"),
              ("Timestamp", self.get_timestamp())]
    string_to_sign = ""
    for (key, val) in params:
        string_to_sign += "{}={}&".format(quote_plus(key), quote_plus(val))
    string_to_sign = "GET\nwebservices.amazon.com\n/onca/xml\n" + string_to_sign[:-1]
    print(string_to_sign)
    print()
    url_params = urlencode(params)
    signature = base64.b64encode(
        unhexlify(self.sign(str.encode(SECRECT_KEY), string_to_sign))).decode()
    print(quote_plus(signature))
    url = "{}?{}&Signature={}".format(self.api, url_params, quote_plus(signature))
    # print(self.sign(str.encode(SECRECT_KEY), string_to_sign))
    print(url)







