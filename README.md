generate pngs caption by usign Salesforce blip-image-captioning-large model\
outputs exported in a csv file
Two approach: \
1.app_large.py --> run model downloaded in local - Require pytorch, transformers lib installed (NOT recommended)\
1.app_large.py --> run hosted model w/ inference API serverless -- need free API token from HuggingFace (easier for prototyping - RECOMMENDED)
