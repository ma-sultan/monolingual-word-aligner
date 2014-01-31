# Monolingual Word Aligner for English

This is a word aligner for English: given two English sentences, it aligns related words in the two sentences. It exploits the semantic and contextual similarities of the words to make alignment decisions.

## Requirements
a. Python **NLTK**  
b. The [Python wrapper for Stanford CoreNLP](https://github.com/dasmith/stanford-corenlp-python)  

## Installation and Usage
a. Install the above tools.  
b. Download the aligner:  
	  git clone https://github.com/ma-sultan/English-Word-Aligner.git  
c. Change line 100 of corenlp.py:  
	  from "rel, left, right = map(lambda x: remove_id(x), split_entry)"  
	  to "rel, left, right = map(lambda x: x, split_entry)".  
d. Run the corenlp.py script to launch the server:  
	  python corenlp.py  
e. To see the aligner in action, run **testAlign.py**. (Word indexing starts at 1.)
