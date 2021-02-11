class A:

    def __init__(self):
        pass
    
    def var_1(self):
        self.x = '77'
        return self.x

class B(A):
    
    def __init__(self):
        pass
        
    def var_2(self):
        self.y = '88'
        return self.y

result = B()
f = result.var_2()

print(f)

result.var_1()
d = result.var_1()

print(d, f)











