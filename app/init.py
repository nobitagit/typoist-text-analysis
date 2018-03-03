import re
from functools import reduce

my_str = "one two three. A test. a re"
words = my_str.split(". ")

# Scoring logic
# To each finger we associate a score:
# thumbs: 1
# index: 1
# middle: 2
# ring: 3
# pinky: 4
#
# To each required motion we add 1 point
# so that it means that all home row letters will
# get 0 as increment (no motion).
# Every letter on top row will receive the score
# associated with the finger + 1.
# Same for the bottom row.
# Index fingers are special cased as they have one more
# column each  (T-G-B and Y-H-N), so they receive +1 for this column.
# Pinky fingers get +1 for each non-column letter (such as [, |, TAB ecc).
# Number row gets +2
# All other chars get +2
# Capital letters get +2

maxScore = 7
scores = {
  'q': 5,
  'w': 4,
  'e': 3,
  'r': 2,
  't': 3,
  'y': 3,
  'u': 2,
  'i': 3,
  'o': 4,
  'p': 5,
  'a': 4,
  's': 3,
  'd': 2,
  'f': 1,
  'g': 2,
  'h': 2,
  'j': 1,
  'k': 2,
  'l': 3,
  ';': 4,
  'z': 5,
  'x': 4,
  'c': 3,
  'v': 2,
  'b': 3,
  'n': 3,
  'm': 2,
  ',': 3,
  '.': 4,
  '/': 5,
  '1': 6,
  '2': 5,
  '3': 4,
  '4': 3,
  '5': 4,
  '6': 4,
  '7': 3,
  '8': 4,
  '9': 5,
  '0': 6,
  ' ': 1
}

def to_score(ch):
  if ch in scores:
    if ch.isupper():
      return scores[ch] + 2
    else:
      return scores[ch]
  return maxScore

scored = list(map(to_score, my_str))
aggregate = reduce(lambda x, y: x + y, scored, 0)

print(aggregate)

text_coll = open("testfile.txt", "r").read()


# for a given sentence calcultate the charactoers score
def score_sentence(sentence):
    scored = list(map(to_score, sentence))
    aggregate = reduce(lambda x, y: x + y, scored, 0)
    return aggregate

def process_text(coll):
    sentences = coll.split(". ")
    ret = []
    for sentence in sentences:
        ret.append({
            'text': sentence,
            'score': score_sentence(sentence)
        })
    return ret

print(process_text(text_coll))
