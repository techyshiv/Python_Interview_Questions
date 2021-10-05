## Q1. Difference Between PEP vs PIP vs PyPi ?.
## A1. 
    PEP(Python Enhancement Proposal) : It is a guideline to format code.
    PIP(Package Installed for Python)
    PyPi(Python Package Index Stored)

## Q2. What is the Difference between Pickling and Unpickling ?.
## A2.    
      Pickling : In Python ,the pickle module Accept any python object and transform it into a string representation and dumps it into a file using a dump function.This process is known as pickling the function used for this process is pickle.dump().

       Unpickling : The Process of Reteriving Original Python object from the stroed string representation is called Unpickling.The function used for this process is pickle.load().

## Q3. What is Gil in Python ?.
## A3. 
       Gil Or Global Interpreter Lock is mutex used to limit access to python objects it synchronizes threads and prevents them to running at the same time.

## Q4. What is the difference between del and remove in the list ?.
## A4. 
      del : del removes all the elements of a list within a given range.
            Syntax : del list[start:end]
      remove : It remove the first occurance of a particular chracter.
            Syntax : list.remove(element)
      
## Q5. Are arguments in python passed by value or passed by reference ?.
## A5. Arguments are passed in python by reference .This means that any change made within a function is reflected in the original object.
## Ex :
```python
def func(l):
    l[0] = 3
l = [1,2,3,4]
func(l)
print(l)

##Output : [3,2,3,4]
```              

## Q6.For a Given Array determine whether a given array can be partitioned into two subarray such that the sum of elements in both arrays is the same.
        1. 
            Input : [1,5,11,5]
            Output : true
            The array can be partitioned as {1, 5, 5} and {11}
        2.
           Input : [1, 5, 3]
           Output : false
           The array cannot be partitioned into equal sum arrays. 

## Q7. For Given Two String find Return Length of Longest Common Subsequence.
## A7. 
      Input 👍: String-1: abcdh
                String-2: abedfhg
      Output : 4 (abdh)

## Q8. What is the output of this Program.
```python
globvar = 0
def set_globvar_to_one():
    global globvar 
    globvar = 1
def print_globvar():
    print(globvar)
set_globvar_to_one()
print_globvar()
```

## Q9. Given two non-negative integers n1 and n2, where n1<n2. The task is to find the total number of integers in the range [n1, n2](both inclusive) which have no repeated digits.
## Explanation : 
               For example:
               Suppose n1=11 and n2=15.
            There is the number 11, which has repeated digits, but 12, 13, 14 and 15 have no repeated digits. So, the output is 4.

            Example1:
            Input:
                    11 — Vlaue of n1
                    15 — value of n2
            Output:
                4
            Example 2:

            Input:
                101 — value of n1
                200 — value of n2

            Output:
                72

## Q.10. A chocolate factory is packing chocolates into the packets. The chocolate packets here represent an array arrt of N number of integer values. The task is to find the empty packets(0) of chocolate and push it to the end of the conveyor belt(array).
 
## Explanation : For Example:

    N=7 and arr = [4,5,0,1.9,0,5,0].
    There are 3 empty packets in the given set. These 3 empty packets represented as O should be pushed towards the end of the array

    Example 1:
    Input:

        6
        — Value of N.
        [6,0,1,8,0,2] – Element of arr[0] to arr[N-1], While input each element is separated by newline

    Output:

        6 1 8 2 0 0

## Oops Question:Which Oops Concept is Used in this Program ?.
## Ans : Polymorphism.
```python
class Bird:
    
    def intro(self):
        print("There are many types of birds.")
  
    def flight(self):
        print("Most of the birds can fly but some cannot.")
  
class sparrow(Bird):
    
    def flight(self):
        print("Sparrows can fly.")
  
class ostrich(Bird):
  
    def flight(self):
        print("Ostriches cannot fly.")
  
obj_bird = Bird()
obj_spr = sparrow()
obj_ost = ostrich()
  
obj_bird.intro()
obj_bird.flight()
  
obj_spr.intro()
obj_spr.flight()
  
obj_ost.intro()
obj_ost.flight()
```