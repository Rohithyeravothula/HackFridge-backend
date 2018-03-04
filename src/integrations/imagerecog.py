import requests
import json
import _pickle as pickle
import binascii

subscription_key = "127b284d2078484ca39996a634e718a1"
print("remove this before commit")

class ImageRecog:
    def __init__(self):
        ""

    def get_ingredients(self, img_data=None):
        vision_base_url = "https://westcentralus.api.cognitive.microsoft.com/vision/v1.0/"
        vision_analyze_url = vision_base_url + "analyze"
        img_data = open("../../resources/fridge1.jpeg", "rb").read()
        headers = {'Ocp-Apim-Subscription-Key': subscription_key,
                   "Content-Type": "application/octet-stream"}
        params = {'visualFeatures': 'tags'}
        req = requests.post(vision_analyze_url, headers=headers, params=params, data=img_data)
        content = req.json()
        tags = []
        if content:
            for tag_dict in content["tags"]:
                if tag_dict["confidence"] > 0.5:
                    tags.append(tag_dict["name"])
        return tags
