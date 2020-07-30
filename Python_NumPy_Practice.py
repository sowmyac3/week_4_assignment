#PYTHON NUMPY:


#IMPORT NUMPY:
import numpy as np

#TASK 1 - Array Indexing:for the following arrays, print the possible numbers:

arr = np.array([1,2,3,4,5,6,7,8])
print(arr)
# It should print = [1 2 3 4 5 6 7 8]
print(arr[1:5])
# It should print = [2 3 4 5]

arr1 = np.array([[1,2,3,4],[5,6,7,8]])
print(arr1)
# It should print = [[1 2 3 4] [5 6 7 8]]
print(arr1[0:2,1:3])
# It should print = [[2 3][6 7]]

arr2 = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(arr2)
# It should print = [[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]]
print(arr2[1,1,1])
# It should print = 11
print(arr2[0:2,0,0:2])
# It should print = [[1 2][7 8]]

#TASK 2 - Array Slicing: for the following array, print the possible numbers:

arr3 = np.array([1,2,3,4,5,6])
print(arr3)
# It should print [1 2 3 4 5 6]
print(arr3[1:5])
# It should print = [2 3 4 5]
print(arr3[:3])
# It should print = [1 2 3]
print(arr3[2:])
# It should print = [3 4 5 6]

#TASK 3 - Iteration: For each array write code to reach the actual values, the scalars (1,2,3,4...)

arr4 = np.array([1,2,3,4,5])
for x in np.nditer(arr4):
    print(x)

arr5 = np.array([[1,2,3],[4,5,6]])
for x in np.nditer(arr5):
    print(x)

arr6 = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
for x in np.nditer(arr6):
    print(x)
#OR...
for x in arr6:
    for y in x:
        for z in y:
            print(z)

#TASK 4 - Split Arrays: Split the array in both cases in 2 ways!!

arr7 = np.array([1,2,3,4,5,6,7,8])
#Example 1:
newarr = np.array_split(arr7,4)
print(newarr)
#It should print:[array([1, 2]), array([3, 4]), array([5, 6]), array([7, 8])]
#Or...
print(newarr[0])
print(newarr[1])
print(newarr[2])
print(newarr[3])
# It should print [1 2] [3 4] [5 6] [7 8]

#Example 2:
newarr1 = np.array_split(arr7,3)
print(newarr1)
# It should print:[array([1, 2, 3]), array([4, 5, 6]), array([7, 8])]
#Or...
print(newarr1[0])
print(newarr1[1])
print(newarr1[2])
# It should print: [1 2 3][4 5 6] [7 8]

#TASK 5 - Array filtering: Write code to print every value which is higher than 30.

arr8 =np.array([5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100])

filter_arr = []

for element in arr8:
    if element > 30:
        filter_arr.append(True)
    else:
        filter_arr.append(False)

newarr2 = arr8[filter_arr]

print(filter_arr)
# It should print:[False, False, False, False, False, False, True, True, True, True, True, True, True, True, True, True, True, True, True, True]
print(newarr2)
# It should print:[ 35  40  45  50  55  60  65  70  75  80  85  90  95 100]







