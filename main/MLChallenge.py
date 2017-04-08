from __future__ import division
from collections import Counter
import nltk # sudo pip install -U nltk (linux) or pip install nltk (windows)
# Before execute for the first time, uncomment the code line bellow, 
# execute the code, wait to finish and comment the code bellow  again
# nltk.download('punkt')

WORDS = [''] # You can put here your another words list (empty by default)
WORDS1 = nltk.corpus.brown.words() # You can put here your words list, like a good dictionary in your language

COUNTS = Counter(WORDS)
COUNTS1 = Counter(WORDS1)

def pdist_good_turing_hack(counter, onecounter, base=1/26., prior=1e-8):
    """The probability of word, given evidence from the counter.
    For unknown words, look at the one-counts from onecounter, based on length.
    This gets ideas from Good-Turing, but doesn't implement all of it.
    prior is an additional factor to make unknowns less likely.
    base is how much we attenuate probability for each letter beyond longest."""
    N = sum(counter.values())
    N2 = sum(onecounter.values())
    lengths = map(len, [w for w in onecounter if onecounter[w] == 1])
    ones = Counter(lengths)
    longest = max(ones)
    return (lambda word: 
            counter[word] / N if (word in counter) 
            else prior * (ones[len(word)] / N2 or 
                          ones[longest] / N2 * base ** (len(word)-longest)))

def memo(f):
    "Memoize function f, whose args must all be hashable."
    cache = {}
    def fmemo(*args):
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]
    fmemo.cache = cache
    return fmemo

P = pdist_good_turing_hack(COUNTS1, COUNTS)

def Pwords2(words, prev='<S>'):
    "The probability of a sequence of words, using bigram data, given prev word."
    return product(cPword(w, (prev if (i == 0) else words[i-1]))
         for (i, w) in enumerate(words))
    
def cPword(word, prev):
    "Conditional probability of word, given previous word."
    return P(word) / 2

def product(nums):
    "Multiply the numbers together.  (Like `sum`, but with multiplication.)"
    result = 1
    for x in nums:
        result *= x
    return result


def splits(text, start=0, L=20):
    "Return a list of all (first, rest) pairs; start <= len(first) <= L."
    return [(text[:i], text[i:]) 
            for i in range(start, min(len(text), L)+1)]
    

def segment(text, prev='<S>'):
    "Return a list of words that is the most probable segmentation of text."
    if not text: 
        return []
    else:
        candidates = ([first] + segment(rest, first) 
                      for (first, rest) in splits(text, 1))
        return max(candidates, key=lambda words: Pwords2(words, prev))
    
segment = memo(segment)

segment.cache.clear()
segmentedList = segment('thisisazqbhjhsyefvvjqctest')

# Test to check if some word is available at the dictionary or not
# print [bigram for bigram in COUNTS1 if bigram.endswith('tim')]

print ' '.join(str(e.strip()) for e in segmentedList)


