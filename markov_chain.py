#!/usr/bin/env python

import markovify

# Read text file, replace new lines with spaces, and save to variable
with open ("padula.txt", "r") as myfile:
      padula_text=myfile.read().replace('\n', '')

# Build the model.
text_model = markovify.Text(padula_text)

# Print five randomly-generated sentences
for i in range(5):
    print(text_model.make_sentence())

# Print three randomly-generated sentences of no more than 140 characters
for i in range(3):
    print(text_model.make_short_sentence(140))

