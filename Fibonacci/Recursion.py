# Fibonacci with Recursion

num1=0
num2=1
print(num1, end=" ")
print(num2, end=" ")
count = 2
def fibonacci(num1, num2):
    global count

    if count<=19:
        sum=num1+num2
        print(sum,end=" ")
        count+=1
        num1=num2
        num2=sum
        fibonacci(num1,num2)
fibonacci(num1, num2)