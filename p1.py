# Name: The sum of two elements.
# Definition: Given an array of integers nums and an integer target, return indices of the two
# numbers such that they add up to the target.
# You may assume that each input would have exactly one solution, and you may not use the same
# element twice.
# You can return the answer in any order.
# Example 1:
# Input: nums = [2,7,11,15], target = 9

# ----------- code ----------------

# main execution start here...
# ask user to enter the size of array and then check negative number or not 
# if negative number then exit the program
sizeArr=input("Enter array size :")
if(int(sizeArr)<=0) :
    print("Invaild Input...")
elif(int(sizeArr)<2):
    print("Minimun size of array must be 2....")
else:
    target=input("Target num")
    print("Enter array elements of array :")
    numArr=[]
    sum=0
    # ask user to enter the all elements of array
    for i in range(0,int(sizeArr)):
        numArr.append(int(input()))
    for i in range(0,int(sizeArr)):
        for j in range(0,int(sizeArr)):
            if(numsArr[i] + numArr[j] == target):
                print(i,j)

# ------ end of program -------------------