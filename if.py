#1
month ={
    '1'" 'january','2': 'february','3': 'march','4':'april',
    '5': 'may','6':'june','7':'july','8':'august',
    '9':'swptember','10':'october','11':'november','12':,'december'
}
month_number=input("enter a number between 1 and 12:")
for x in month:
    if x==month_number:
        print(f"the corresponding mpnth is {month[x]}")

#2
user_num1=int(input("enter number1:"))
user_num2=int(input("enter number 2:"))
if user_num1=user_num2:
print("equal")
else:
print("unequal")
if user_num1-user_num2>0:
    print("the first number is greater")
    print("tajinder\n"*5)
else:
    print("the second number is greater and first is smaller")
    print("puri\n"*3)

    #3
str1 = input("enter first string:")
str2 = input("enter second string:")
if str1 == str2:
    print("both strings are equal")
else:
    print("both strings are not equal")
#5
n = int(input("enter a number:"))
total=(n*(n+1))/2
print(f"the sum till our number is {total}")

#6
number=int(input("enter a number:"))
print("even numbers are:")
for i in range(1,number):
    if i%2==0:
        print(i)
        #7
        num = int(input("enter a number:"))
        op = input("enter op (+ or -):")
if op == "+":
    for i in range(0,num):
        print(i,end=",")
elif op =="-":
    for i in range(num,0,-1):
        print(i,end=",")