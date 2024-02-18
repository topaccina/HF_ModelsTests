import glob
import pandas as pd
import requests
import os

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
API_KEY = os.getenv("API_TOKEN")


API_URL = (
    "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-large"
)
headers = {"Authorization": f"Bearer {API_KEY}"}


def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()


generated_text = []
pngList = glob.glob("./png/*.png")
for png in pngList:
    resp = query(png)
    generated_text.append(resp[0]["generated_text"])
    print(resp)

output = pd.DataFrame({"pngFileName": pngList, "Caption": generated_text})

# # export to a csv
output.to_csv("./output/generated_text_large_API.csv", index=False)
