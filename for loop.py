#1
n = int(input("enter a number:"))
total=(n*(n+1))/2
print(f"the sum till our number is{total}")
#2 
num = int(input("enter a number"))
for i in range(1, 11):
    print(num, "*", i, "=", num * i)
    #4
    user_string=input("enter a number:")
    user_string=list(user_string)
    reverse_string=user_string[::-1]
    if reverse_string==user_string:
print("the given number is palindrome")
else:
print("the given number is not palindrome")
#5
for i in range(1,50):
    if i%3==0 and i%5==0 :
        print("fizzbuzz")
elif i%3==0:
print("fizz")
elif i%5==0:
print("buzz")
else:
print(i)





