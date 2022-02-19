import json

def data_to_json(path:str, output:str):
    """
        Converts a text data file into a JSON file that openAI can understand
        
        Inputs:
         - path: Path to the input text file
         - output: Path to the output json file
    """
    
    data = load_data(path)
    with open(output, 'w') as f:
        json.dump(data, f, indent=4)

def load_data(path:str):
    """
        Loads in a text data file and converts it into json data

        Inputs:
         - path: Path to the input text file

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
            
            if '--SmartContract--' in l:
                if (contract != ''):
                    sample = {
                        'text': contract,
                        'label': classification
                    }

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

    return samples

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