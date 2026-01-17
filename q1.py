#1
friends_name=["A","B","C","d","e"]
new_friend=input("give a name of your friend:")
friends_name.append(new_friend)
imp_frnd=input("whose your most imp friend?")
friends_name.insert(0,imp_frnd)
print(friends_name)

#

num=[]
for x in range(11):
    num.append(x)
print(num)

#3

list=[1,10,100,3,6,8]
list.insert(33,59)
list.append(5)
print(list)
print(f"length of list is",len(list))

#4
n=[]
string=["abcdf","gftygyt","as","wie","geht","entschuldigung"]
for x in string:
if len(x)<4:
n.append(x)
print(n)

#5
list_a=1,2,3,4
list_b=2,3,4,5
ans=[i for i in list_a if i in list_b]
print(ans)