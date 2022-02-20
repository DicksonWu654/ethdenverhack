from numpy import array
from glob import glob
from pathlib import Path
import itertools
import numpy as np

def generate_dataset(dataset_path:str, samples_per_script:int) -> array:

    # array of tupels, (input_string, label) 
    dataset = []
    
    safe_scripts = glob(f'{dataset_path}/scripts/safe/*.txt')
    vun_scripts = glob(f'{dataset_path}/scripts/vun/*.txt')
    name_files = glob(f'{dataset_path}/names/*.txt')

    # load data from files
    names = {}
    for file in name_files:
        name = Path(file).stem
        samples = [n.lower()for n in open(file).read().splitlines() if not n.startswith('#')]
        names[name] = samples

    scripts = []
    for file in safe_scripts:
        sample = open(file).read().lower()
        scripts.append((sample, 0))

    for file in vun_scripts:
        sample = open(file).read().lower()
        scripts.append((sample, 1))

    filled_scripts = []
    filled_scripts_labels = []
    for script in scripts:

        script_text_raw = script[0]
        script_label = script[1]
        
        # pre-process the script
        script_text_raw = " ".join(script_text_raw.split())
        script_text = []

        # replace all entities with their permitations
        for word in script_text_raw.split():
            if word.startswith('{') and word.endswith('}'):
                # the word is a entity, swap it out for the permutations
                entity = word[1:-1]
                
                script_text.append(names[entity])
            else:
                script_text.append([word])

        filled_scripts.append(script_text)
        filled_scripts_labels.append(script_label)

    # generate all permitations
    print('Loading permutations')
    permutations = []
    permutation_labels = []
    for sample, label in zip(filled_scripts, filled_scripts_labels):
        generated = list(itertools.product(*sample))
        permutations.extend(generated)
        permutation_labels.append([label] * len(generated))

    # generate the dataset
    Xs = [" ".join(p) for p in permutations]
    ys = permutation_labels

    Xs_file = open('Xs.txt', 'w')
    for x in Xs:
        np.savetxt(x, Xs_file)

    ys_file = open('ys.txt', 'w')
    for y in ys:
        np.save_txt(y, ys_file)