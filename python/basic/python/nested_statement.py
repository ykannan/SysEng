#LEGB
#Local : local namespace
#Enclosing function locals: Namespace in localscope for enclosed functions
#Global (Module) : assigned at the top level of the modeule or built-inodule
#Built-in (Python): open,range, syntax error

#Example
name = 'global '       # 3 enclosed function local variable
def greet ():
    name = 'function local'       # 2 enclosed function local variable
    def hello():
        name = 'local'           # 1 local variable
        print('hello ' +name)   
    hello()

greet()

#Example 2
x = 50
def func():
    global x
    print(f"X is {x}")
    
    x=200
    print(f"X is {x}")

func()