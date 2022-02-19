import openai
import json

import dataset_loader as loader

loader.data_to_json('./samples.txt', './samples.json')

# key = loader.load_key('./key.txt')
# openai.api_key = key

# context = loader.load_data('./context.txt')
# response = openai.Completion.create(engine='text-babbage-001', prompt=context, max_tokens=6)

# print(response)