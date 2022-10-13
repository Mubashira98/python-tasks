'''
1. Write a Python program to find a list of integers with exactly two occurrences of nineteen
and at least three occurrences of five
Input:
[19, 19, 15, 5, 3, 5, 5, 2]
Output:
True
'''

# numbers=[]
# for i in range(int(input("enter no. of values"))):
#     n=int(input("enter value"))
#     numbers.append(n)
# print(numbers)
# if numbers.count(19)==2 and numbers.count(5)>=3:
#     print("True")
# else:
#     print("False")

'''
2. Write a Python program to find a pair with highest product from a given array of integers.
Examples :
Input: arr[] = {1, 2, 3, 4, 7, 0, 8, 4}
Output: {7,8}
Input: arr[] = {0, -1, -2, -4, 5, 0, -6}
Output: {-4, -6}
'''
# def product_fun():
#     arr= {1, 2, 3, 4, 7, 0, 8, 4}
#     arr=list(arr)
#     l=len(arr)
#     print(arr)
#     products=[]
#     x=arr[0]
#     y=arr[1]
#
#     for i in range(0,l):
#         for j in range(i+1,l):
#             n=arr[i]*arr[j]
#             if n>(x*y):
#                 x=arr[i]
#                 y=arr[j]
#     return x,y
#
# find=product_fun()
# print(set(find))

'''
3.Write a Python program that accept a list of integers and check the length and the fifth element.
Return true if the length of the list is 8 and fifth element occurs thrice in the said list. 
Input:
[19, 19, 15, 5, 5, 5, 1, 2]
Output:
True
Input:
[19, 15, 5, 7, 5, 5, 2]
Output:
'''
# integers=[]
# for i in range(int(input("enter no. of integers"))):
#     integers.append(int(input("enter value")))
# n=integers.count(integers[4])
# if len(integers)==8 and integers.count(integers[4])==3:
#     print("True")
# else:
#     print("False")


'''
4. ARRAY CHALLENGE
Have the function ArrayChallenge(arr) take the array of numbers stored in arr which will contain
integers that represent the amount in dollars that a single stock is worth,and return the maximum
profit that could have been made by buying stock on day X and selling stock on day Y where Y&gt;X .For
example if array is [44,30,24,32,35,30,40,38,15] then your program should return 16 because at
index 2 the stock was worth $24 and at index 6 the stock was then worth $40, so if you brought the
stock at $24 and sold it at $40, you would have made a profit of $16,which is the maximum profit
that could hve been made with this list of stock prices.
If there is not profit that could have been made with the stock prices,then your program should
return -1. For example arr is [10,9,8,2] then your program should return -1

Example
Input: [10,12,4,5,9]
Output:5
'''

# arr=[10,9,8,2,12]
# profit=[]
# l=len(arr)
# for i in range(0,l):
#     for j in range(i+1,l):
#         if arr[j]>arr[i]:
#             p=arr[j]-arr[i]
#             profit.append(p)
#         else:
#             profit.append(-1)
# print(max(profit))

'''python pragram to print all integers within the range 100-200 whose sum of digits is an even number.'''
# sum=0
# for num in range(100,201):
#     number=str(num)
#     sum=(int(number[0])+int(number[1])+int(number[2]))
#     if sum%2==0:
#         print(num)

'''
program to find the largest number and its position in a list without using built-in functions.
'''
list=[3,8,1,7,2,9,5,4]
largest=list[0]
for i in range(len(list)):
    if list[i]>largest:
        largest=list[i]
        index=i
print("The largest element is", largest,"and its position is at", index, "th index")


































