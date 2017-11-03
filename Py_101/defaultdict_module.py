from collections import defaultdict


# split
sentence = "The red for jumped over the fence and ran to the zoo for food"
words = sentence.split(' ')

reg_dict = {}
for word in words:
    if word in reg_dict:
        reg_dict[word] += 1
    else:
        reg_dict[word] = 1

print(reg_dict)


default_dict = defaultdict(int)
for word in words:
    default_dict[word] += 1

print(default_dict)
