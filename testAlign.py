from aligner import *

sentence1 = 'For example , an electron that has been accelerated to 0.78 times the speed of light has a de Broglie wavelength of 2 pm ( 2 times 10-12 m ) , which is about 100 times smaller than the typical interatomic distance in a solid .'
sentence2 = 'Interatomic distance in a solid is smaller than an electron .'

print align(sentence1, sentence2)

