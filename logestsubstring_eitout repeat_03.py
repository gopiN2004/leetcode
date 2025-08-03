def not_repeat(s):
    current=""
    longest=0
    for ch in s:
        if ch in current:
            index = current.index(ch)
            current =current[index+1:]
        current +=ch
        longest =max(longest,len(current))
    return longest
s=input("input a string:")
result= not_repeat(s)
print(result)
