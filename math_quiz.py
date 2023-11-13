import random

def generate_random_numbers(min, max):
    """
    Generate and return a random number within the given range    
    :param min : minimum value of the range 
    :type  min : int
    :param max : maximum value of the range 
    :type  max : int
    
    """
    return random.randint(min, max)

def select_random_operator():
    """
    Select and return a random mathematical operator
    """
    return random.choice(['+', '-', '*'])

def quiz_builder(number1, number2, operator):
    """
    generate and return mathematical problem statement and answer for the quiz
    
    :param number1  : random number 1
    :type  number1  : int
    :param number2  : random number 2 
    :type  number2  : int
    :param operator : mathematical operator
    :type  operator : char
    
    """
    
    #Building mathematical problem statement for the quiz
    problem = f"{number1} {operator} {number2}"
    
    #Genarating answer for the problem statement
    if operator == '+':
        answer = number1 + number2
    elif operator == '-': 
        answer = number1 - number2
    else: 
        answer = number1 * number2
    return problem, answer

def math_quiz():
    """
    implementation of a mathematical quiz game 
    """
    score = 0
    total_questions = 10

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    #Loop to generate questions 
    for i in range(total_questions):
        #generate and store random numbers for mathematical problem statement
        number1 = generate_random_numbers(1, 10)
        number2 = generate_random_numbers(1, 5)
        
        #Select and store operator for mathematical problem statement
        operator = select_random_operator()
        
        #Build and store mathematical problem statement and answer
        problem, answer = quiz_builder(number1, number2, operator)
 
        print(f"\nQuestion: {problem}")
        
        #Get user answer input and typecast to integer data type 
        user_answer = input("Your answer: ")
        
        #Check whether the given input is a valid number 
        try:
          user_answer = int(user_answer)
        except ValueError:
            print ("Value Error: Enter a valid integer value")
            continue
        
        #Check if user answer is correct and update the score
        if user_answer == answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {answer}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
