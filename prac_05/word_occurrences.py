"""
Word Occurrences
Estimate: 21 minutes
Actual:   27 minutes
"""

from operator import itemgetter

words_in_string = input("Text: ")
words = words_in_string.split()
word_counts = {}
for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

max_length = max([len(word) for word in word_counts])
for word, count in sorted(word_counts.items(), key=itemgetter(0)):
    print(f"{word:{max_length}} : {count}")