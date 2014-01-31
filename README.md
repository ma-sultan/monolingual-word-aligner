# Monolingual Word Aligner for English

This is a word aligner for English: given two English sentences, it aligns related words in the two sentences. It exploits the semantic and contextual similarities of the words to make alignment decisions.

## Requirements
a. Python **NLTK**  
b. The [Python wrapper for Stanford CoreNLP](https://github.com/dasmith/stanford-corenlp-python)  

## Installation and Usage
a. Install the required software.  
b. Change line 100 of corenlp.py:  
	from "rel, left, right = map(lambda x: remove_id(x), split_entry)"  
	to "rel, left, right = map(lambda x: x, split_entry)".  
c. Run the corenlp.py script to launch the server:  
	python corenlp.py  
d. To see the aligner in action, run **testAlign.py**. (Word indexing starts at 1.)
