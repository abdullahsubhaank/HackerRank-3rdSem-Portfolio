from collections import Counter

def matchingStrings(strings, queries):
    counts = Counter(strings)
    return [counts[q] for q in queries]
