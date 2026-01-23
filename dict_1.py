#1
sentence=input('give me a sentence:')
words=sentence.split()
dict_1={}
word_count=1
for i in words:
    if i in dict_1:
        dict_1[i]+=1
    else:
        dict_1[i]=word_count
print(dict_1)

#2
student_details={
    "alice":46
    "bob":45
    "jai":78
    "henry":45
}
avg_marks=0
n=0
for k,v in student_details.items():
    avg_marks+=v
    n+=1
avg_marks=avg_marks/n
print(f"the average marks are:{avg_marks}")
for k,v in student_details.items():
    if v>avg_marks:
        print(f"congrats {k} you scored higher than average marks")

#3
dict_2={"a":50,"b":30,"c":70}
dict_3={"b":60,"c":65,"d":40}
merged_dict={}
for k,v in dict_2.items():
    if k in dict_3:
        if v>dict_3[k]:
            merged_dict[k]=v
        else:
            merged_dict[k]=dict_3[k]
    else:
        merged_dict[k]=v
for k,v in dict_3.items():
    if k not in dict_2:
        merged_dict[k]=v
print(merged_dict)

#4
person_info={
    'name':'bob', 'city':'hyderabad', 'course':'machine learning'}
id_length=0
output=""
for i in person_info:
 if id_length<len(i):
     id_length=len(i)
     output=i
print(output)

#5
data = {
    'a': 5,
    'b': 15,
    'c': 30,
    'd': 55,
    'e': 50,
    'f': 10
}

filtered_data = {k: v for k, v in data.items() 
                 if 10 <= v <= 50}

print(filtered_data)

#6
votes = {}
n = int(input("Enter number of voters: "))
for i in range(n):
    candidate = input(f"Enter vote {i + 1}: ").strip()
    votes[candidate] = votes.get(candidate, 0) + 1
print("\nVote Count:")
for candidate, count in votes.items():
    print(candidate, ":", count)
winner = max(votes, key=votes.get)
print("\nWinner:", winner)
print("Votes received:", votes[winner])

#7
data = {'a': 10, 'b': 20, 'c': 30}
update = {'b': 200, 'c': 300}
for key in data:
    if key in update:
        data[key] = update[key]
print(data)