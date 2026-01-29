movie_list=[ { "name": "Forrest Gump", "year": 1994, "duration": 142, "genres": ["Drama", "Romance"] },
{ "name": "Avengers: Endgame", "year": 2019, "duration": 181, "genres": ["Action",
"Adventure", "Drama"] }, { "name": "Back to the Future", "year": 1985, "duration": 114,
"genres": ["Adventure", "Comedy", "Sci-Fi"] } ]
print("welcome to movies")

new_dict={}
flag=True
def input_something(inp):
    user_input = input(inp)
    while user_input =="":
        print("input cannot be empty. please try again.")
        user_input = input(inp)
    return user_input
def input_int(prompt): 
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("input should only be integer. please try again.")

while flag:
    user_choice=input("choose [a]dd, [l]ist, [s]earch, [v]iew, [d]elete or [q]uit:").lower()
    if user_choice=='a':
        genre_list=[]
        m_name=input_something("enter movie's name:")
        m_year=input_int("enter movie's year:")
        m_duration=input_int("enter duration in minutes:")
        m_genre_num=input_int("enter genre number:")
        while m_genre_num==0:
            print("you should enter atleast one genre!")
            m_genre_num = input_int("enter genre numbers")
        new_dict["name"]=m_name
        new_dict["year"]=m_year
        new_dict["duration"]=m_duration
        for i in range(m_genre_num):
            m_genre = input_something("enter genre").title()
            genre_list.append(m_genre)
        new_dict["genre"]=genre_list
        print('movie added')
        movie_list.append(new_dict)
    elif user_choice=="l":
        index=0
        if movie_list:
            for ind,j in enumerate(movie_list,start=1):


                index=index+1
                print(f"{ind} {j['name']};{i['year']}")
        else:
            print("no movies saved")
    elif user_choice=="s":
        search_term=input_something("give the name of the movie to search:").lower()
        if movie_list:
            index=1
            for i in movie_list:
                if search_term in i["name"].lower():
                    print(f"({index}) {i["name"]}({i["year"]})")
                    index+=1
        else:
            print("the list is empty")
    elif user_choice == "V":
        if movie_list:
            try:
                index_number=input_int("give me an  index number for the movie..")
                index_number-=1
                print(movie_list[index_number])
            except IndexError:
                print("invalid index number")
    elif user_choice =="d":
        if movie_list:
            try:
                index_number = input_int("give me an index number for the movie to delete:")
                index_number -=1
                movie_list.remove(movie_list[index_number])
                print("movie deleted")
            except IndexError:
                print("invalid index number") 
    elif user_choice == "q":
        print("goodbye!!")
        break
    else:
        print("please enter only from the values suggested!!")

                
        