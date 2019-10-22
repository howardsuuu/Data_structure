class Robot():
	def __init__(self, name, color, weight, lookingAt=""):
		self.name = name
		self.color = color
		self.weight = weight
		self.lookingAt = lookingAt

	def introduceSelf(self):
		print('Name: '+ self.name)
		print('Color: '+ self.color)
		print('Weight: ', self.weight)
		print('Looking_At: '+ self.lookingAt)

	def __str__(self):
		result = 'Name: '+ self.name + "\n"
		result += 'Color: '+ self.color + "\n"
		result += 'Weight: ' +  str(self.weight) + "\n"
		result += 'Looking_At: '+ self.lookingAt
		return result


class Person():
	"""docstring for Person"""
	def __init__(self, name, personality, isSitting, robotOwned):
		
		self.name = name
		self.personality = personality
		self.isSitting = isSitting
		self.robotOwned = robotOwned
	
	def person_info(self):
		print('Person_Nmae: '+self.name)
		print('Personality: '+self.personality)
		print('Is sitting: ', self.isSitting)
		print('Own_robot: ', self.robotOwned)
		# self.robotOwned.introduceSelf()

	def sitDown(self):
		self.isSitting = True

	def standUp(self):
		self.isSitting = False



r1 = Robot('Tom', 'red', 30, 'r2')
r2 = Robot('Jerry', 'blue', 40, 'r3')
r3 = Robot('Hans', 'purple', 50, 'r1')

'''
r1 = Robot('Tom', 'red', 30)
r2 = Robot('Jerry', 'blue', 40)
r3 = Robot('Hans', 'purple', 50)

r1.set_lookingAt("r2")
r2.set_lookingAt("r3")
r3.set_lookingAt("r1")
'''


p1 = Person("Alice", "aggressive", True, r2)
p2 = Person("Becky", "aggressive", False, r1)
p3 = Person("Howard", "polite", True, r3)

p3.person_info()
	








