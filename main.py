import openai
import json

import dataset_loader as loader

# loader.load_data('./samples.txt')
print(json.dumps(json.loads(loader.load_data('./samples.txt')), indent=4))

# key = loader.load_key('./key.txt')
# openai.api_key = key

# context = loader.load_data('./context.txt')
# response = openai.Completion.create(engine='text-babbage-001', prompt=context, max_tokens=6)

# print(response)