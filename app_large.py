from transformers import pipeline
import glob
import pandas as pd
import warnings


warnings.filterwarnings("ignore")

# specify task and model
pipe = pipeline("image-to-text", model="Salesforce/blip-image-captioning-large")
# get all the pngs to process
pngList = glob.glob("./png/*.png")
# call the model
response = pipe(pngList)
# parse the output. Create a dataframe w/ generated captions for each png
generated_text = []
for resp in response:
    generated_text.append(resp[0]["generated_text"])
    print(resp[0]["generated_text"])


output = pd.DataFrame({"pngFileName": pngList, "Caption": generated_text})

# export to a csv
output.to_csv("./output/generated_text_large.csv", index=False)
