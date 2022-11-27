print("#"*60)
import time
import random
k1=time.time()
while True:
    print('''# Press:
> S or s to start
> E or e to exit''')
    print("-"*25)
    a1=input("Enter the command: ")
    if a1 in "Ss":
        n1=[1,2,3,4,5,6,7,8,9,0]
        n2=["+","-","*"]
        print("-"*60)
        a=int(input("Enter the no. of rounds:"))
        print("-"*60)
        f1=0
        for i in range(1,a+1):
            u1=0
            while u1<1:
                r1=random.choice(n1)
                r2=random.choice(n1)
                r3=random.choice(n2)
                if r1>r2:
                    u1=u1+1
                    print("# Enter value of (Round-"+str(i)+"): "+str(r1)+str(r3)+str(r2))
                    b=int(input(">>> "))
                    if r3=="+":
                        m1=int(r1+r2)
                    elif r3=="-":
                        m1=int(r1-r2)
                    else:
                        m1=int(r1*r2)
                    if b==m1:
                        if i<a:
                            print("-"*40)
                    else:
                        u2=0
                        while u2<1:
                            f1=f1+1
                            print()
                            print("! Wrong answer...")
                            print("-Enter value of (Round-"+str(i)+"): "+str(r1)+str(r3)+str(r2))
                            b2=int(input("> "))
                            if b2==m1:
                                print("-"*40)
                                u2=u2+1
        k2=time.time()
        k=int(k2-k1)
        print("*"*60)
        print(" "*20,"."*5,"SUMMARY","."*5)
        print("-","Total round:",a)
        print("-","Wrong answer:",f1)
        print("-","Effective round(Right+Wrong):",a+f1)
        print()
        print("-"*20,k//60,"Minute",k%60,"Second","-"*20)
        print()
        print("#"*60)
    elif a1 in "Ee":
        print("#"*60)
        break
    else:
        print("*"*60)
        print(" "*15,"! Invalid input, Try again...")
        print("*"*60)