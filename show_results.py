"""
Goal: A function that reads data from a file and prints in a different format.
"""
import csv
def show_results(filename):
    with open(filename) as source:
        filecontent = csv.reader(source)
        for row in filecontent:
            print(row[0], row[2], "-", row[3], row[1])
show_results("hemulencup.csv")
