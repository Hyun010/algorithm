word=''
for w in input():
    if w.isupper():
        word+=w.lower()
    else:
        word+=w.upper()
print(word)