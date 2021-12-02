#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#1. Make a calculator using Python with addition , subtraction ,multiplication ,division and power.
# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        
        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    
    else:
        print("Invalid Input")


# In[2]:


#2. Write a program to check if there is any numeric value in list using for loop.
test_list = [ 1, 6, 3, 5, 3, 4 ]
 
print("Checking if 4 exists in list ( using loop ) : ")
 
# Checking if 4 exists in list
# using loop
for i in test_list:
    if(i == 4) :
        print ("Element Exists")


# In[1]:


#3. Write a Python script to add a key to a dictionary.
d = {'key':'value'}
print(d)
d['mynewkey'] = 'mynewvalue'
print(d)


# In[4]:


#4. Write a Python program to sum all the numeric items in a dictionary.
# Function to print sum
def returnSum(myDict):
     
    list = []
    for i in myDict:
        list.append(myDict[i])
    final = sum(list)
     
    return final
 
dict = {'a': 500, 'b':800, 'c':1000}
print("Sum :", returnSum(dict))


# In[5]:


#5. Write a program to identify duplicate values from list.
def Repeat(x):
    _size = len(x)
    repeated = []
    for i in range(_size):
        k = i + 1
        for j in range(k, _size):
            if x[i] == x[j] and x[i] not in repeated:
                repeated.append(x[i])
    return repeated
 

list1 = [10, 20, 30, 20, 20, 30, 40,
         50, -20, 60, 60, -20, -20]
print (Repeat(list1))


# In[9]:


#6. Write a Python script to check if a given key already exists in a dictionary.

d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def is_key_present(x):
  if x in d:
      print('Key is present in the dictionary')
  else:
      print('Key is not present in the dictionary')
is_key_present(4)
is_key_present(25)


# In[ ]:




