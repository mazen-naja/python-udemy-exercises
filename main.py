#Excersie 1

def calculate_sum(a,b):
    sum=a+b
    return  str(sum)

a=2
b=3
print(a,"+",b,"=",calculate_sum(a,b))



#Excersie 2

def is_square_root(x,y):
    
    if (abs(y)==abs(x)**0.5):
        return True
    return False

x=4
y=2
print (is_square_root(x,y))
