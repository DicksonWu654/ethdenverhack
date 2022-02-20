import json
import os
from xml.etree.ElementInclude import include

#? File system integrations
def data_to_json(path:str, output:str):
    """
        Converts a text data file into a JSON file that openAI can understand
        
        Inputs:
         - path: Path to the input text file
         - output: Path to the output json file

        Outputs:
         - data: Data in JSON format
         - writes to the output file
    """
    
    data = load_data(path)

    if os.path.exists(output):
        os.remove(output)
    else:
        print('fail case')

    with open(output, 'w') as f:
        for d in data:
            f.write(f'{d}\n')

    return data

def load_data(path:str, include_comments:bool = False):
    """
        Loads in a text data file and converts it into json data

        Inputs:
         - path: Path to the input text file
         - include_comments: whether to include comments or not

        Outputs:
         - samples: Array of classification sample/label pairs
    """

    with open(path) as f:
        raw_lines = f.readlines()

        samples = []

        getting_contract = False
        getting_classification = False

        contract = ''
        classification = ''
        for l in raw_lines:
            if l.startswith('#'):
                continue

            if not include_comments:
                l = l.split('//')[0]
            
            if '--SmartContract--' in l:
                if (contract != ''):
                    sample = {
                        "text": " ".join(contract.split()), # removes whitespace + new line tags
                        "label": classification
                    }
                    sample = json.dumps(sample)
                    samples.append(sample)
                    contract = ''
                    classification = ''

                getting_contract = True
                getting_classification = False
                continue

            if '--Classification--' in l:
                getting_classification = True
                getting_contract = False
                continue

            if getting_contract:
                contract += l

            if getting_classification:
                classification += l[:-1]
                getting_classification = False
    
    sample = {
        "text": " ".join(contract.split()), # removes whitespace + new line tags
        "label": classification
    }
    sample = json.dumps(sample)
    samples.append(sample)
    
    return samples

def load_sample(path: str):
    """
        Loads in a single sample prompt

        Inputs:
         - path: path to the text file
        
        Outputs:
         - sample: single line string sample smart contract 
    """

    sample = ''

    with open(path) as f:
        raw_lines = f.readlines()

        for l in raw_lines:
            if l.startswith('#'):
                continue

            sample += l

    sample = " ".join(sample.split())
    return sample

def load_json(path:str):
    """
        Loads in a json file for data

        Inputs:
         - path: Path to the json data

        Outputs:
         - data: Json data
    """

    with open(path) as f:
        data = json.load(f)
        return data

def load_key(path:str):
    """
        Loads in an API key

        Inputs:
         - path: Path to the txt file containing the key

        Outputs:
         - key: API key
    """

    with open(path) as f:
        key = f.read()
        return key