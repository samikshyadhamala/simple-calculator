a = int(input("enter first no= "))
b = int(input("enter second no= "))
c=input("enter any operator (+,-,*,/)=")
if(c=="+"):
    print("the sum of",a,"and",b,"is",a+b,".")
elif(c=="*"):
    print("the multiplication of",a,"and",b,"is",a*b,".") 
elif(c=="/"):
    if(a>b):
        print("the division of",a,"by",b,"is",a/b,".")   
    else:
        print("the division of",b,"by",a,"is",b/a,".")  
elif c=="-":
    if(a>b):
        print("the subtraction of",b,"from",a,"is",a-b,".")    
    else:
        d=(input("do u want to print negative value or absolute value?(neg/abs)="))
        if(d=="neg"):
           print("the subtraction of",b,"from",a,"is",a-b,".")
        else:
            print("the subtraction of",b,"from",a,"is",b-a,".")
else:
    print("invalid symbol")              
