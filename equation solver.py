import random

def main():
    x = random.randint(-100,100)

    equation = 3 * x + 4
    
    while equation != 0:
        print(
            'Trying to find the root of the equation at ' + str(x)
        )
        print(
            'At ' + str(x) + ' value of the equation will be ' + str(equation)
        )
        x = random.randint(-100,100)
        equation = 4 * x + 4

        continue
        
        
    
    else:
        print(
            'Trying to find the root of the equation at ' + str(x)
        )
        print(
            'At ' + str(x) + ' the given equation will be zero!'
        )
    
main()