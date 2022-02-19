import openai
import time
# from transformers import GPT2TokenizerFast

import dataset_loader as loader

# preprocess and save data
SAMPLES = 'samples.txt'
KEY = 'key.txt'
DATA = 'data.jsonl'

loader.data_to_json(SAMPLES, DATA)

# initialize the openAI API
key = loader.load_key(KEY)
openai.api_key = key

# preform classification
openai_file = openai.File.create(
    file=open("data.jsonl"), 
    purpose="classifications"
)



print(openai_file)

# Make sure the labels are formatted correctly.
labels = ["yes", "no"]

# Query the /classifications endpoint
query = loader.load_sample('./test.txt')
# print(query)
time.sleep(10)
result = openai.Classification.create(
    file=openai_file["id"],
    query=query,
    search_model="ada",
    model="davinci",
    max_examples=10,
    # labels=labels,
    # logprobs=3,  # Here we set it to be len(labels) + 1, but it can be larger.
    # expand=["completion"],
)
print(result)
print(result['label'])