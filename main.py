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



#Excersie 3

def odd_sum(n):
    abs(n)
    sum1=0
    while (n>0):
        if(n%2!=0):
            sum1 =sum1+n
        n= n-1
    return sum1


#Excersise 4

def sum(user_input):

    str1=""
    sum1=0
    i=0
    while(i<user_input):
        sum1+=user_input
        if(i==user_input-1):
            str1=str1+str(user_input)+" = "+str(sum1)
        elif(i<user_input):
            str1=str1+str(user_input)+" + "

        i+=1
  
    return str1



#Excersise 5
def cubic_root(n):
    # n is a positive integer
    i = 0
    pr = 0
    prold=0
    while i < n:
        pr = i**3
        if pr > n:
            prold=(i-1)**3
            break
        i=i+1
    if(pr>n):
      return  print(i-1,", not exact with a difference of", n-prold)
    else: return print (i-1,"exact!")

userinput = int(input("Enter a number: "))
cubic_root(userinput)
