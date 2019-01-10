
class classification(object):
	#a method (the constructor -gets executed automatically when you construct the object)
	#method gets executed when you create an instance of an object
	def __init__(self, animal):
		self.animal = animal

	def classify(self):
		return self.animal

class question(object):
	def __init__(self, question, no = None, yes = None):
		self.question = question
		self.answers = {
			"n":	no,
			"y":	yes
		}

	def classify(self):
		while True:
			prompt = "%s? [%s] " % (self.question, "/".join(self.answers.keys()))
			answer = input(prompt).lower()
			if answer in self.answers:
				next_obj = self.answers[answer]
				if next_obj == None:
					return None
				return next_obj.classify()
			print("Answer %s" % (" or ".join(self.answers.keys())))

def make_animals():
	root = question("Is it a mammal",
		no = question("Does it live in the sea",
		    no = question("Does it hop",
				no = classification("Penguin"),
				yes = classification("Frog")
			),
			yes = classification("Fish")
		),
		yes = question("Does it live in trees",
			no = classification("Rabbit"),
			yes = classification("Squirrel")
		)
	)
	return root

animals = make_animals()
animal = animals.classify()
if animal == None:
	print("Could not come up with an answer")
else:
	print("Animal is: "+animal)
