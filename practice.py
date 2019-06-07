

l=[input() for i in range(int(input()))]
def wrapper(f):
    def fun(l):
        f(["+91 "+c[-10:-5]+" "+c[-5:] for c in l ])
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l),sep="\n")

sort_phone(l)



