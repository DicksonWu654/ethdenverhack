import openai

import dataset_loader as loader

# preprocess and save data
SAMPLES = 'samples.txt'
KEY = 'key.txt'
DATA = 'data.jsonl'

loader.data_to_json(SAMPLES, DATA)

# # initialize the openAI API
# key = loader.load_key(KEY)
# openai.api_key = key

# # preform classification
# print(open(DATA).readlines())
# openai.File.create(
#     file=open(DATA), 
#     purpose="classifications"
# )

