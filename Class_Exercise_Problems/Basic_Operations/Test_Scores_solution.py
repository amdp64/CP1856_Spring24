# -*- coding: utf-8 -*-
"""
Created on Wed May 15 16:43:57 2024

@author: Arun.Rameshbabu
"""

print("The Test Scores program\n")
print("Enter 3 test scores")
print('='*40)
total_score = 0
# Another way of doing addition - whlie saving the sum back to the same variable.
total_score += int(input("Enter test score: "))
total_score += int(input("Enter test score: "))
total_score += int(input("Enter test score: "))
# test_score_1 = int(input("Enter test score: "))
# test_score_2 = int(input("Enter test score: "))
# test_score_3 = int(input("Enter test score: "))
print('='*40)

# Doing the calculations
average_score = total_score / 3

# Print out the results
print(f"Total Score:\t {total_score}")
print(f"Average Score:\t {int(average_score)}\n")
print("Bye!")
