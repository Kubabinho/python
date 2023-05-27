n = int(input('give christmas trees height: '))
def christTree(n):
    for i in range(n):
        print(' ' * (n - (i + 1)),'+' * (2*i+1))
christTree(n)