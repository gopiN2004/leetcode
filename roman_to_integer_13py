def RomanToInt(s):
    roman={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    total=0
    pre_value=0

    for char in reversed(s):
        value=roman[char]
        if value < pre_value:
           total-=value
        else:
            total+=value
        pre_value=value
    return total
s=input():#IVXLCDM only
print(RomanToInt(s))
