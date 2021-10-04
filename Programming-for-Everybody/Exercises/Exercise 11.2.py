'''
Finding Numbers in a Haystack

In this assignment you will read through and parse a file with text and numbers. You will extract all the numbers in the file and compute the sum of the numbers.

Data Files
    We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

Sample data: http://py4e-data.dr-chuck.net/regex_sum_42.txt (There are 90 values with a sum=445833)
Actual data: http://py4e-data.dr-chuck.net/regex_sum_1324191.txt (There are 84 values and the sum ends with 855)
These links open in a new window. Make sure to save the file into the same folder as you will be writing your Python program. Note: Each student will have a distinct data file for the assignment - so only use your own data file for analysis.

Data Format
    The file contains much of the text from the introduction of the textbook except that random numbers are inserted throughout the text.The numbers can appear anywhere in the line. There can be any number of numbers in each line (including none).

Handling The Data
    The basic outline of this problem is to read the file, look for integers using the re.findall(), looking for a regular expression of '[0-9]+' and then converting the extracted strings to integers and summing up the integers.

Turn in Assignment
    Enter the sum from the actual data and your Python code.
'''

import re
hand = open('regex_sum_1324191.txt')
nums = []

for line in hand:
    line = line.strip()
    stuff = re.findall('([0-9]+)', line)
    if len(stuff) == 0 : continue
    nums.append(stuff)
    
number = 0
for list1 in nums:
    for list2 in list1:
        number = int(list2) + number

print(number)