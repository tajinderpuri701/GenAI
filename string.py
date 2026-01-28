#1
def first_last_two(s):
    s = s.lower() 
    if len(s) < 2:
        return "not a valid string"
    return s[:2] + s[-2:]

print(first_last_two("Coder roots"))  
print(first_last_two("New year"))     
print(first_last_two("A"))           

#2
def swap_first_chars(s1, s2):
    if not s1 or not s2:
        return "Invalid input"

    new_s1 = s2[0] + s1[1:]
    new_s2 = s1[0] + s2[1:]

    return new_s1 + " " + new_s2

print(swap_first_chars("coder", "roots")) 

#3
def add_ing_or_ly(s):
    if len(s) < 3:
        return s
    elif s.endswith("ing"):
        return s + "ly"
    else:
        return s + "ing"

print(add_ing_or_ly("abc"))   
print(add_ing_or_ly("string"))
print(add_ing_or_ly("hi"))   

#4
def remove_nth_char(s, n):
    if n < 0 or n >= len(s):
        return "Invalid index"
    return s[:n] + s[n+1:]

print(remove_nth_char("python", 2))  
print(remove_nth_char("hello", 0))   
print(remove_nth_char("world", 4))  



