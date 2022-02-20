# EthDenver - Deus Ex Securitas

Using machine learning to automatically audit smart contracts. NLP models can classify solidity scripts by their vulnerability and could even point out what lines contribute to the vulnerable nature of the code. 
Since we're using machine learning, we bring the cost of an audit from days to seconds, and thousands of dollars to nothing - allowing everyone to have access to security.
This leads to an overall safer and more secure blockchain ecosystem and creates a security floor that no project should fall below.

## Re-entry attacks
Re-entry attacks can occur when a function can be interrupted in the middle of its execution and subsequently re-initiated.  Thus, assuming both runs can complete without errors, the attacker can run specific parts of a script an arbitrary number of times before progressing.

## Our backend
We elected to use the pre-trained NLP model, BERT, to predict the vulnerabilities of solidity contracts. With this model, leveraging its pre-existing [knowledge], we were able to create a more effective and generalizable system.  While we only trained our model on re-entry attacks, given past experience and the results from existing papers we can confidently say that if provided with more training data it could easily generalize to classify more unique vulnerabilities. Furthermore, our data augmentation strategies involved minimal human labour and produced a substantial number of training samples.  Using a mad-libs-inspired approach we can generate ten unique, sensible samples for each example we provided.  This makes it theoretically feasible for us to implement many more vulnerabilities into our detection algorithm.

## Our future plans
Once we’ve built a model that can determine the vulnerability of a given smart contract, it’s not that hard to reverse-engineer the model’s process and figure out what parts of the input contract triggered the response.  This means that we can assign each word a score based on how likely it is to contribute to the vulnerability, effectively highlighting the parts of the contract that are vulnerable to exploits.

Right now we’ve got a model that can detect re-entry attacks. It’s only a matter of data and resources to scale up to all types of known exploits. We aren’t stopping there, we can even reverse-engineer the model’s process and highlight parts of the code that are vulnerable to the exploit. Additionally, we can even train models which are capable of generalizing unknown types of exploits, surpassing human-level performance.

## Online Demo
Coming soon
