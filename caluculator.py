class caluculator:
    def my_cal(self):
        self.a = int(input(" please enter the number"))
        self.b = int(input(" Please enter the number"))
    def my_add(self):
        addition = self.a + self.b
        print (addition)
    def my_sub(self):
        sub = self.a - self.b
        print(sub)
    def my_mul(self):
        mul = self.a * self.b
        print(mul)
    def my_div(self):
        div = self.a // self.b
        print(div)

A1 = caluculator()
A1.my_cal()
A1.my_add()
A1.my_sub()
A1.my_mul()
A1.my_div()



