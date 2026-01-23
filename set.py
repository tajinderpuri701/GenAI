#1
friday = {'alice','bob','charlie'}
saturday = {'charlie','david','eve'}
all_guests=friday.union(saturday)
print(f'person attending all night are{all_guests}')
all_nights=friday.intersection(saturday)
print(f'the person attending both nights is {all_nights}')

#2
data = [1, 2, 2, 3, 4, 4, ,4 , 5]
data=set(data)
data.add(6)
print(data)

#3
library_book = {'hobbit','1984','gatsby','odyssey','hamlet'}
checked_out = {'1984','hamlet'}
book_sitting=library_book-checked_out
print(book_sitting)
if "don quixote" not in library_book:
    library_book.add('don quixote')
print(library_book)

#4
user_permissions={'read','write'}
admin_reqs={'read','write','execute'}
if admin_reqs.issubset(user_permissions):
    print('the user has all the permissions required for admin access')
else:
    print(f'{str(admin_req-user_permission)} are missing')

    #5
    logs = {
        "404":[10, 12, 15, 20],
        "500":[12, 20, 22, 25],
        "403":[10, 20, 30]
}
new_set={k for k in logs["404"] if k in logs["500"] and k in logs["403"]}
print(f"server ids that experienced every type of error :{new_set}")
critical_servers={k for k in logs["500"] if k not in logs["404"]}
print(f"servers that experienced a 500 error but never exprienced 404 error:{critical_servers}")

