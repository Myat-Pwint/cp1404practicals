"""
Word Occurrences
Estimate: 25 minutes
Actual: 35 minutes
"""

counts = {}
text = input("Text: ")

for word in text.split():
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1

max_width = max(len(word) for word in counts.keys())

print("Text: ", text)
for word in sorted(counts):
    count = counts[word]
    print(f"{word:{max_width}} : {count}")
