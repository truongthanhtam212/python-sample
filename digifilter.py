"""
The function must remove all values from the list that are higher than the threshold.
"""
def filter_errors(a, b):
    for x in a[:]:
        if x > b:
            a.remove(x)