class NameBuilder():
    def __init__(self):
        self.digit=list(map(int,input().strip("[]").split(",")))
        self.numbers=int("".join(map(str,self.digit[::-1])))

    def get_number(self):
        return self.numbers
    def sum_both(self):
        l1 = self.get_number()
        l2 = NameBuilder().get_number()
        total= l1+l2
        result=list(map(int,str(total)[::-1]))
        return result
obj =NameBuilder()
final=obj.sum_both()
print(final)




