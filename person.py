class Person:
    def __init__(self, age, color):
        self.age = age
        self.color = color
    def write(self, world):
        return (str(self.age) + ":" + world )

zhang = Person(12, "white")
li = Person(23, "black")
print("zhang:", zhang.age)
print("li:",li.age)
z = zhang.write("wwww")
print(z)
ll = li.write("llll")
print(ll)