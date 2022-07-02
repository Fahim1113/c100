class Car(object):
  def __init__(self, brand, model, topSpeed, colour):
    self.brand = brand
    self.model = model
    self.topSpeed = topSpeed
    self.colour = colour
  def setBrand(self, brand):
    self.brand = brand
  def setModel(self, model):
    self.model = model
  def setTopSpeed(self, topSpeed):
    self.topSpeed = topSpeed
  def setColour(self, colour):
    self.colour = colour
  def getSpecifications(self, brand, model, topSpeed, colour):
    a = []
    if brand:
      a.append(self.brand)
    if model:
      a.append(self.model)
    if topSpeed:
      a.append(str(self.topSpeed))
    if colour:
      a.append(self.colour)
    return '\n'.join(a)
car = Car('Tesla', 'Model 3', 100, 'White')
print(car.getSpecifications(True, True, False, False))