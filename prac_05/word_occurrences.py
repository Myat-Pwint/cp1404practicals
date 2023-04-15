"""
Word Occurrences
Estimate: 30 minutes
Actual:minutes
"""

count = {}
text = input("Text: ")

for word in text.split():
    if word in count:
        count[word] += 1
    else:
        count[word] = 1



print("Text: ", text)
for word, count in count.items():
    print(word, ":", count)
