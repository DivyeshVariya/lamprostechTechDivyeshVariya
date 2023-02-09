# Name: Single Integer
# Definition: Given a non-empty array of integers nums, every element appears twice except for
# one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra
# space.

# ---------code--------------
# this function use for find the single number into array
# logic for finding single number is to XOR the all elements and 
# XOR of same number id will be 0
def findSingleNum(numArr,sizeArr):
    response = numArr[0]
    for i in range(1,int(sizeArr)):
        response = response ^ numArr[i]
    return response

# main execution start here...
# ask user to enter the size of array and then check negative number or not 
# if negative number then exit the program
sizeArr=input("Enter the size of Array :")
if(int(sizeArr)<=0) :
    print("Invaild Input...")
else:
    print("Enter array elements of array :")
    numArr=[]
    # ask user to enter the all elements of array
    for i in range(0,int(sizeArr)):
        numArr.append(int(input()))
    print("SIgnle Number is : " + str(findSingleNum(numArr,sizeArr))) #call the function for output

# ------ end of program -------------------
