name= ("pelden nidup")
print(name)
greeting="hello, " + name +"!"
print(greeting)
greeting_f= f"hello, {name}!"
print(greeting_f)
name_length = len(name)
print(name_length)
age=19
age_str= str(age)
message="i am" + age_str + " years old."
print(message)
non_num_str = "Hello"
try:
    non_num_int = int(non_num_str)
    print(non_num_int)
except ValueError as e:
    print(f"Error: {e}")