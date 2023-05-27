def char(string):
    dic1 = {}
    for i in string:
        dic1[i] = dic1.get(i,0) + 1
    return dic1
n = str(input('give the sentence for char check: '))
dict = char(n)
char_number = sorted(dict)
for i in char_number:
    print(i, dict.get(i))
print(char(n))
