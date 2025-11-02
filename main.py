import random;

def addition_expression(addend1, addend2):
    return (addend1 + addend2)

def subtraction_expression(minuend, subtrahend):
    return (minuend - subtrahend)

def multiplication_expression(multiplicand, multiplier):
    return (multiplicand * multiplier)

def division_expression(dividend, divisor):
    return (dividend / divisor)

if __name__ == "__main__":
    while True:
        term1 = random.randint(0, 100)
        term2 = random.randint(0, 100)

        quit = input("Press Q or q to end this program. Press any other key to continue. ");

        if quit.lower() == "q":
            print("Thank you for playing! Program terminated.")
            break

        option = input(
            "Press + to solve addition problems. \n" + 
            "Press - to solve subtraction problems. \n" + 
            "Press * to solve multiplication problems. \n" + 
            "Press / solve division problems. \n"
            )
        
        match option:
            case "+":
                expression = f"{term1} + {term2} = "
                answer = addition_expression(term1, term2)
            case "-":
                if term1 < term2:
                    swap = term1
                    term1 = term2
                    term2 = swap


                expression = f"{term1} - {term2} = "
                answer = subtraction_expression(term1, term2)
            case "*":
                term1 = random.randint(0, 14)
                term2 = random.randint(0, 14)

                expression = f"{term1} * {term2} = "
                answer = multiplication_expression(term1, term2)
            case "/":

                term1 = random.randint(1, 14)
                term2 = random.randint(1, 14)

                if term1 < term2:
                    swap = term1
                    term1 = term2
                    term2 = swap

                print("Round to the nearest hundredths place [0.00]")

                expression = f"{term1} / {term2} = "
                answer = round(division_expression(term1, term2), 2)


        response = input("Solve this equation: " + expression)

        if answer == float(response):
            print("Congratulations! You got the correct answer.")
            print(expression + response)
        else:
            print("Incorrect answer.")
            print("The correct answer is " + str(answer))