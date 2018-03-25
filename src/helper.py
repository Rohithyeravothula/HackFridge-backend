# # # print(ami.get_timestamp())
# #
# # # sample = """GET
# # # webservices.amazon.com
# # # /onca/xml
# # # AWSAccessKeyId=AKIAIOSFODNN7EXAMPLE&AssociateTag=mytag-20&ItemId=0679722769&Operation=ItemLookup&ResponseGroup=Images%2CItemAttributes%2COffers%2CReviews&Service=AWSECommerceService&Timestamp=2014-08-18T12%3A00%3A00Z&Version=2013-08-01"""
# # #
# # #
# # # single = "GET\nwebservices.amazon.com\n/onca/xml\nAWSAccessKeyId=AKIAI4DBXQLNEU7J4QWA&AssociateTag=7557-20&Keywords=potatoes&Operation=ItemSearch&ResponseGroup=Images%2CItemAttributes%2COffers&SearchIndex=All&Service=AWSECommerceService&Timestamp=2018-03-03T23%3A23%3A46"
# #
# #
# # print("change")
# # single = """GET
# # webservices.amazon.com
# # /onca/xml
# # AWSAccessKeyId=AKIAI4DBXQLNEU7J4QWA&AssociateTag=7557-20&Keywords=potatoes&Operation=ItemSearch&ResponseGroup=Images%2CItemAttributes%2COffers&SearchIndex=All&Service=AWSECommerceService&Timestamp=2018-03-03T23%3A39%3A16"""
# # hexd = hmac.new(str.encode(SECRECT_KEY), single.encode('utf-8'), hashlib.sha256).hexdigest()
# # # print(b2a_base64(unhexlify(hexd)))
# # encoded = base64.b64encode(unhexlify(hexd))
# # print(quote_plus(encoded))
# #
# #
# # def get_products(self, product_name):
# #     params = [("AWSAccessKeyId", SubscriptionId), ("AssociateTag", AssociateTag),
# #               ("Keywords", product_name), ("Operation", "ItemSearch"),
# #               ("ResponseGroup", "Images,ItemAttributes,Offers"),
# #               ("SearchIndex", "All"), ("Service", "AWSECommerceService"),
# #               ("Timestamp", self.get_timestamp())]
# #     string_to_sign = ""
# #     for (key, val) in params:
# #         string_to_sign += "{}={}&".format(quote_plus(key), quote_plus(val))
# #     string_to_sign = "GET\nwebservices.amazon.com\n/onca/xml\n" + string_to_sign[:-1]
# #     print(string_to_sign)
# #     print()
# #     url_params = urlencode(params)
# #     signature = base64.b64encode(
# #         unhexlify(self.sign(str.encode(SECRECT_KEY), string_to_sign))).decode()
# #     print(quote_plus(signature))
# #     url = "{}?{}&Signature={}".format(self.api, url_params, quote_plus(signature))
# #     # print(self.sign(str.encode(SECRECT_KEY), string_to_sign))
# #     print(url)
#
#
#
#
#
#
#
#
# subscription_key = "127b284d2078484ca39996a634e718a1"
#
# AssociateTag = "7557-20"
# SubscriptionId = "AKIAJPCSEBMUPJ2SNTFA"
# SECRECT_KEY = "ySQU3+3NcZqnJDMpBzYIOACB2+fOyWh9y3fIltQ4"
#
# AssociateTag = "7557-20"
# SubscriptionId = "AKIAJPCSEBMUPJ2SNTFA"
# SECRECT_KEY = "ySQU3+3NcZqnJDMpBzYIOACB2+fOyWh9y3fIltQ4"
#
#
# 'Ocp-Apim-Subscription-Key': subscription_key,
#
#
# context = ("../../resources/ssl-cert/hacktech.crt", "../../resources/ssl-cert/hacktech.key")