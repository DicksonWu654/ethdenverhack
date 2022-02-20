import numpy as np

def encode(tokenizer: object, texts: list, max_len: int) -> tuple:
    """
        Encode a sequence of strings using the provided tokenizer.
        Returns an encoded ID and an attention mask
        Inputs: 
         - tokenizer: tokenizer object from the PreTrainedTokenizer class
         - texts:     sequence of strings to be tokenized
         - max_len:   integer controling the maximum number of tokens to tokenize
        
        Outputs:
         - input_ids:      sequence of encoded tokens as a np array
         - attention_mask: sequence of attention masks as a np array
    """

    input = tokenizer(
        texts,
        max_length=max_len,
        padding='max_length',
        truncation=True,
        return_attention_mask=True,
        return_token_type_ids=False,
        return_tensors='np'
    )

    return input['input_ids'], input['attention_mask']