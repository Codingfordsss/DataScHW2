import random

def generate_random_integer(min_value, max_value):
    """
    Generate a random integer between min_value and max_value, inclusive.
    
    Args:
        min_value (int): The minimum possible integer.
        max_value (int): The maximum possible integer.
        
    Returns:
        int: A randomly selected integer between min_value and max_value.
    """
    return random.randint(min_value, max_value)


def choose_random_operator():
    """
    Choose a random mathematical operator from +, -, and *.
    
    Returns:
        str: A randomly selected operator ('+', '-', or '*').
    """
    return random.choice(['+', '-', '*'])


def generate_problem_and_answer(num1, num2, operator):
    """
    Generates a math problem as a string and computes its answer.

    Args:
        num1 (int): The first number in the math problem.
        num2 (int): The second number in the math problem.
        operator (str): The operator for the math problem ('+', '-', or '*').

    Returns:
        tuple: A tuple containing the problem as a string and the correct answer as an integer.
    """
    problem = f"{num1} {operator} {num2}"
    
    # Calculate the answer based on the operator
    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    else:  # operator is '*'
        answer = num1 * num2
    
    return problem, answer


def math_quiz_game():
    """
    Run the math quiz game, where the user is presented with random math problems.
    The user's score is displayed at the end of the game.
    """
    score = 0  # Initialize the user's score
    total_questions = 3  # Total number of questions in the quiz

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        # Generate random numbers and an operator
        num1 = generate_random_integer(1, 10)
        num2 = generate_random_integer(1, 5)  # Ensures num2 is an integer
        operator = choose_random_operator()

        # Generate a math problem and the correct answer
        problem, correct_answer = generate_problem_and_answer(num1, num2, operator)
        
        # Display the problem to the user
        print(f"\nQuestion: {problem}")
        
        # Validate user input with error handling
        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue  # Skip to the next question

        # Check the answer and update the score
        if user_answer == correct_answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {correct_answer}.")

    # Display the final score
    print(f"\nGame over! Your score is: {score}/{total_questions}")

# Run the game if this script is the main program
if __name__ == "__main__":
    math_quiz_game()
