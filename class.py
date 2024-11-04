class person:
  def __init__(self, name, age, gender):
    self.name = name
    self.age = age
    self.gender = gender

  def introduce(self):
    print(f"Hello my name is {self.name} and I am {self.age} years old. I am a {self.gender}.")

person1 = person("John", 25, "male")

person2 = person("Jane", 30, "female")

person1.introduce()
person2.introduce()