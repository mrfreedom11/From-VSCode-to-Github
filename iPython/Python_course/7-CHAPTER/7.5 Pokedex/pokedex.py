class Pokemon():
  def __init__(self , entry , name , types , description , is_caught, level , region , height , weight):
    self.entry = entry
    self.name = name
    self.types = types
    self.description = description
    self.is_caught = is_caught
    self.level = level
    self.region = region
    self.height = height
    self.weight = weight
  def speak(self):
    print(self.name, self.name + '!')
  def display_details(self):
    print("Entry Number:", self.entry)
    print("Name:", self.name)
    print("Type:", ", ".join(self.types))
    print("Description:", self.description)
    print("Level:", self.level)
    print("Region:", self.region)
    print("Height:", self.height, "meters")
    print("Weight:", self.weight, "kilograms")

    if self.is_caught:
        print(f"{self.name} has already been caught!")
    else:
        print(f"{self.name} has not been caught yet!")