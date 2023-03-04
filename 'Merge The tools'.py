def merge_the_tools(string, k):
    t=[string[i:i+k] for i in range(0, len(string), k)]
    j=0
    l=len(t)
    p=""
    for al in range (l):
        for char in t[al]:
            if char not in p:
                p=p+char
        j+=1
        print(p)
        p=""
        
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)