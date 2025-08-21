#search for a number 36 in this tuple using loop.[1,4,9,16,36.....100] 
count=1
while count<=10:
    n=count*count
    count+=1
    if(n==36):
        print(n,count)