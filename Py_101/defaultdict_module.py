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


# _list
my_dict = {}
my_list = [(1234, 100.23), (345, 10.45), (1234, 75.00),
           (345, 222.66), (678, 300.25), (1234, 35.67)]

for acct_num, value in my_list:
    if acct_num in my_dict:
        my_dict[acct_num].append(value)
    else:
        my_dict[acct_num] = [value]


d = defaultdict(list)
for acct_num, value in my_list:
    d[acct_num].append(value)


print(d)


# lambda
animal = defaultdict(lambda: "Monkey")
animal['Sam'] = 'Tiger'
print(animal['Nick'])
print(animal)


# KeyError
x = defaultdict(None)
print(x['Mike'])
