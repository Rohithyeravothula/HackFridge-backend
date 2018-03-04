import requests


class ImageRecog:
    def __init__(self):
        self.vision_analyze_url = "https://southcentralus.api.cognitive.microsoft.com/customvision/v1.1/Prediction/260143c4-e99f-4993-b517-652d0545b2b5/image"

    def get_ingredients(self, img_data=None):
        if not img_data:
            img_data = open("../../resources/fridge1.jpeg", "rb").read()
        headers = {"Prediction-Key": "ffad13a8175144cca69da75e70c72ff4", "Content-Type": "application/octet-stream"}
        req = requests.post(self.vision_analyze_url, headers=headers, data=img_data)
        content = req.json()
        tags = []
        if content:
            for tag_dict in content["Predictions"]:
                tags.append((tag_dict["Tag"], tag_dict["Probability"]))
        tags.sort(key=lambda x: float(x[1]), reverse=True)
        tags = list(map(lambda x: x[0], tags))
        return tags




