#collection : counters, namedtuple, orderedDict, defaultDict, deque

from collections import Counter

words = "The quick brown fox jumps over the lazy dog"
count = Counter(words)
print(count.keys())
print(count.most_common(2))
