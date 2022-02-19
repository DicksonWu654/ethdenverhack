def load_data(path):

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
                        'contract': contract,
                        'classification': classification
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

def load_key(path):

    with open(path) as f:
        key = f.read()
        return key