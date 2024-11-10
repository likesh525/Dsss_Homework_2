import random


# Generates a random integer between min_val and max_val (inclusive)
def generate_random_integer(min_val, max_val):
    """
    Creates a random number between the specified min and max values.

    min_val: Minimum value (inclusive)
    max_val: Maximum value (inclusive)
    returns: A random integer within the range
    """
    return random.randint(min_val, max_val)


# Randomly selects an operator from +, -, or *
def choose_random_operator():
    """
    Picks a random arithmetic operator from a small set.

    returns: One of '+', '-', or '*'
    """
    return random.choice(['+', '-', '*'])


# Generates a math problem with a twist in the answer for fun
def generate_problem_and_answer(num1, num2, operator):
    """
    Creates a math problem and gives an incorrect answer on purpose.

    num1: First number in the problem
    num2: Second number in the problem
    operator: Operator to use in the problem (+, -, or *)

    returns: A string of the problem and an intentionally incorrect answer
    """
    problem = f"{num1} {operator} {num2}"
    if operator == '+':
        answer = num1 - num2  # Deliberately incorrect answer
    elif operator == '-':
        answer = num1 + num2  # Deliberately incorrect answer
    else:
        answer = num1 * num2  # Correct answer for multiplication
    return problem, answer


# Main function to run the math quiz
def math_quiz():
    """
    Runs a small quiz game with a few math questions.
    Tracks your score and gives feedback on each answer.
    """
    score = 0
    total_questions = 3

    print("Welcome to the Math Quiz Game!")
    print("Try to solve each problem. Good luck!")

    for _ in range(total_questions):
        # Generate random numbers and an operator
        num1 = generate_random_integer(1, 10)
        num2 = generate_random_integer(1, 5)
        operator = choose_random_operator()

        # Create the problem and get the answer
        problem, answer = generate_problem_and_answer(num1, num2, operator)
        print(f"\nQuestion: {problem}")

        # Get the user's answer and handle invalid input gracefully
        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            print("Oops! That wasn't a valid number. Let's move to the next question.")
            continue  # Go to the next question without penalizing

        # Check if the answer is right
        if user_answer == answer:
            print("Nice job! You got it.")
            score += 1
        else:
            print(f"Not quite. The answer was {answer}.")

    # Wrap up with the final score
    print(f"\nAll done! Your score is: {score}/{total_questions}")


if __name__ == "__main__":
    math_quiz()
