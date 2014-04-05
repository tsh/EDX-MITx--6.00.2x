"""
You are taking a class that plans to assign final grades based on two midterm quizzes and a final exam. The final grade will be based on 25% for each midterm, and 50% for the final. You are told that the grades on the exams were each uniformly distributed integers:

    Midterm 1: 50 <= grade <= 80

    Midterm 2: 60 <= grade <= 90

    Final Exam: 55 <= grade <= 95

Write a function called sampleQuizzes that implements a Monte Carlo simulation that estimates the probability of a student having a final score >= 70 and <= 75. Assume that 10,000 trials are sufficient to provide an accurate answer.

Note: Do not include any "import" statements in your code. We import the random module for you, and you should not be using any functions from the Pylab module for this problem.
"""

import random

def sampleQuizzes():
    yes = 0
    for e in range(10000):
        mid1 = random.choice(range(50, 80))
        mid2 = random.choice(range(60, 90))
        finalExam = random.randrange(55, 95)
        score = mid1*0.25 + mid2*0.25 + finalExam*0.5
        if score >= 70 and score <= 75:
            yes += 1
    return yes / 10000.0

print sampleQuizzes()
