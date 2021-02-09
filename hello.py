n=int(input("Enter the value of n"));

x=i=0;
y=1;
while i<n:
    print(i);
    x=x+y;
    y=x-y;
    i+=1