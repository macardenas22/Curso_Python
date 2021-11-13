

def run ():
    objetive = int(input('Please choose a number: '))
    epsilon = 0.01 #mistake level accepted 
    step = epsilon**2
    answer = 0.0

    while abs(answer ** 2 - objetive) >= epsilon and answer <= objetive:
        answer += step

    if abs(answer ** 2 - objetive) >= epsilon:
        print(f'The square root Not found of {objetive}')
    else: 
        print(f'The square root of {objetive} is {answer}')



if __name__ == '__main__':
    run()