class City:
    def __init__(self, name, country, population, landmarks):
      self.name = name
      self.country = country
      self.population = population
      self.landmarks = landmarks
tashkent = City(
  name = 'tashkent',
  country = 'Uzbekistan',
  population = 4000000,
  landmarks = ['Maqbara', 'Joy']
)

print(vars(tashkent))