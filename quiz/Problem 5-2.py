__author__ = 'tsh'
"""
Write a procedure called plotQuizzes that produces a plot of the distribution of final scores for all of the trials. Try your best to match exactly how the histogram below looks (including the bins, titles and labels on the axes). Click the image to see a larger version.
Your code should make a call to the function generateScores, which is defined according to the following docstring:
"""
def generateScores(numTrials):
    """
    Runs numTrials trials of score-generation for each of
    three exams (Midterm 1, Midterm 2, and Final Exam).
    Generates uniformly distributed scores for each of
    the three exams, then calculates the final score and
    appends it to a list of scores.

    Returns: A list of numTrials scores.
    """

import pylab
def plotQuizzes():
    pylab.hist(generateScores(10000), bins=7)
    pylab.title("Distribution of scores")
    pylab.xlabel("Final Score")
    pylab.ylabel("Number of Trials")
    pylab.show()


plotQuizzes()

