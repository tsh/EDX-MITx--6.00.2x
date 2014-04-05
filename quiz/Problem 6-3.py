"""
Suppose you have a six sided die, with sides number 1 through 6, and you roll it several times.
What is the probability that the first time you observe a 1 is on the second roll? 5/36

You observe that the probability of first seeing a 1 on the n-th roll decreases as n increases.
You would like to know the smallest number of rolls such that this probability is less than some limit.
Complete the Python procedure, probTest, to compute this.
"""

def probTest(limit):
    roll = 1
    while True:
        prob = (5**(roll-1)) / (6.0**roll)
        if prob < limit:
            return roll
        roll += 1

print probTest(0.1)


