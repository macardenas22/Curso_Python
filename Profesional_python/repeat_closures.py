#string y numero -> generar la cantidad de repeticiones del Str,e.g: hola 3 ->holaholahola

def make_repeater_of(n):
	def repeater(string):
		assert type(string) == str, "solo puedes utilizar cadenas"
		return string*n
	return repeater


def run():
	repeat_10= make_repeater_of(10)
	print(repeat_10(" Platzi"))
	repeat_5 = make_repeater_of(5)
	print(repeat_5(" Hola"))
	


if __name__ == "__main__":
	run()

