class Hashira():
	
	def __init__(self, name, school):
		self.name = name 
		self.school = school 

	def print_name(self):
		print(self.name)

	def priclass Hashira():
	
	def __init__(self, name, school):
		self.name = name 
		self.school = school 

	def print_name(self):
		print(self.name)

	def print_school(self):
		print(self.school)

class Persona(Hashira):
	"""
	clase que representa a un hashira
	"""

	def __init__(self, velocidad, fuerza, respiracion, resistencia, estilo):
		""" Constructor de clase hashira"""
		self.velocidad = velocidad
		self.fuerza = fuerza
		self.respiracion = respiracion
		self.resistencia = resistencia
		self.estilo = estilo


test_I = Hashira('Rengoku', 'Escuela del fuego')
test_II = Persona(4, 5, 'Fuego', 90, 'Llama')

 
hashiras = [ {'name': 'Rengoku', 'school': 'Pilar de la llama'}, {'name': 'Tomioka', 'school': 'Pilar del agua'}]
for hashira in hashiras:
	hashira_item =	Hashira(hashira['name'], hashira['school'])
	hashira_item.print_name()
	hashira_item.print_school()nt_school(self):
		print(self.school)

class Persona(Hashira):
	"""
	clase que representa a un hashira
	"""

	def __init__(self, velocidad, fuerza, respiracion, resistencia, estilo):
		""" Constructor de clase hashira"""
		self.velocidad = velocidad
		self.fuerza = fuerza
		self.respiracion = respiracion
		self.resistencia = resistencia
		self.estilo = estilo


test_I = Hashira('Rengoku', 'Escuela del fuego')
test_II = Persona(4, 5, 'Fuego', 90, 'Llama')

 
hashiras = [ {'name': 'Rengoku', 'school': 'Pilar de la llama'}, {'name': 'Tomioka', 'school': 'Pilar del agua'}]
for hashira in hashiras:
	hashira_item =	Hashira(hashira['name'], hashira['school'])
	hashira_item.print_name()
	hashira_item.print_school()