class human:

    # class altribute
    species = "human"

    # intance altribute
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def sing(self,song):
        return f"{self.name} sings {song}"

    def dance(self):
        return f"{self.name} is now dancing"

# instantiate the parrot class
king = human("king" ,67)
sam = human("sam" ,45)

print(f"king is a {king.species}")
print(f"sam is a {sam.species}")

print(f"{king.name} is {king.age} years old")
print(f"{sam.name} is {sam.age} years old")

print(king.sing("happy"))
print(sam.dance())