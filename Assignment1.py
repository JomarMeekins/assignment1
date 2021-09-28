# Name: Jomar Meekins
# Course: CS151, Prof. Mehri
# Date: September, 27, 2021
# Programming Assignment: 1
# Program Inputs: [Dimensions: (width, length, and height of the room in feet]
# Program Outputs: [the total area of four walls and ceiling to decide the amount of paint and primer needed in gallons]
# 1 Identifying variables and their values
# 2 Ask user to provide intergers for width, length, and height in feet
# 3 output: area of all the walls and ceiling decides the amount of paint and primer needed

# Formula
# 1
width = int(input("Please enter width in ft: "))

# 2
length = int(input("Please enter length in ft: "))

# 3
height = int(input("Please enter height in ft: "))

# 4
area = 2*(width + length)*height
gallons_in_primer = (area/200)

# 5
gallons_in_paint = (area/350)

# 6
print("The area of the walls and ceiling", area, "amount of paint,", gallons_in_paint, "amount of primer", gallons_in_primer)