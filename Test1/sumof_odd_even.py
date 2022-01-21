num=int(input("Enter the number"))

def odd(num1):
    sum=0
    num=num1
    while num!=0:
      r=num%10
      if r%2!=0:
        sum+=r
      num=num//10  
      
    return sum

def even(num1):
    sum1=0
    num=num1
    while num!=0:
      r=num%10
      if r%2==0:
        sum1+=r
      num=num//10  

    return sum1  

print("Sum of even digits:-",even(num))  
print("Sum of odd digits:-",odd(num)) 

