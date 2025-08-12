def greet():
    print("hello,world!")
    greet()

def greet(name):
    print(f"hello, {name}!")
    greet("pelden")