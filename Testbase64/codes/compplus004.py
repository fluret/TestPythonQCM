words1 = ['a', 'b']
words2 = ['x', 'y', 'z']
combinations = {(w1, w2) for w1 in words1 for w2 in words2}
print(combinations)