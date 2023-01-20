class A:
    def __init__(self):
       self.x = 10

# class B(A):
#     def __init__(self):
#         self.y = self.x +5
# print(B).y #Ошибка! 'NoneType' object has no attribute 'y'
# правильно:

class B(A):
    def __init__(self):
        super().__init__() #не забудь!!
        self.y = self.x +5

print(B().y) #15