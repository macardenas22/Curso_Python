def divisors(num):
    divisors=[]
    for i in range (1, num+1): 
        if num % i == 0:
            divisors.append(i)
    return divisors
        
def run():
    num = input("ingresa un numero...")
    assert num.isnumeric() and int(num) > 0, "Debes ingresar un numero positivo mayor a cero"
    print(divisors(int(num)))
    print("termino mi programa")


if __name__ == "__main__":
    run()
