# EthDenver - Deus Ex Securitas

Using machine learning to automatically audit smart contracts. NLP models are able to classify solidity scripts by their vulnerability and could even point out what lines contribute to the vulnerable nature of the code. 
Since we're using machine learning, we bring the cost of an audit from days to seconds, and thousands of dollars to nothing - allowing everyone to have access to security.
This leads to an overall safer and more secure blockchain ecosystem and creates a security floor that no project should fall below.

## Re-entry attacks
Re-entry attacks can occur when a function can be interupted in the middle of its execution and subsequently re-initiated.  Thus, assuming both runs can complete without errors, the attacker can run specific parts of a script an arbitrary number of times before progressing.

## Out backend
Using a fine-tuned DistilBert model with a classification head allowed us to quickly and easily train, test, and deploy our model.  This resulted in a system with a validaion accuracy of 96%.  While likely biased due to the small dataset, numerous mesures were taken to minimize the effect of overfitting.

## Our future plans
Right now we've got a model that can detect re-entry attacks. It's only a matter of data and resources to scale up to all types of known exploits. We but aren't stopping there, we can even reverse-engineer the model's process and highlight parts of the code which are vulnerable to the exploit. Additionally we can even train models which are capable of generalizing unknown types of exploits, surpassing human level performance.

## Online Demo
Coming soon
