def find(list, value):
    lenght = len(list)
    j = 0
    index = []
    for i in (list):
        if i == value:
            index.append(j)
        j+=1
        if j > lenght:
            break
    print(index)
l1 = ['word','fsdgdsgdsg','fdsgsdgdgds','word','sdgdsgsdg','sgsdgsdgds','sdfsdf','safsdf','word','sddsg','word']
print(l1)
value = str(input('give the word: '))
find(l1, value)