# Fibonacci series with for loop

num1=0
num2=1
print(num1, end=" ")
print(num2, end=" ")
for i in range(18):
    sum=num1+num2
    print(sum, end=" ")
    num1=num2
    num2=sum
