def f_read(bun,key=0):
    f22=open(bun+"1.csv","r")
    databas=f22.readlines()
    if key==1:
        return databas
    for row in databas:
        row=row.split(",")
        bcd=row[2]
    bcd=eval(bcd)
    f22.close()
    return bcd
def un_data(un,dv):
                                                        
                            f2=open(un+"1.csv","a")
                            f2.write(dv)
                            f2.close()
def f_write(path):
                            f1=open("database.csv","a")
                            f1.write(path)                            
                            f1.close()
def password1(fname,lname,un,password,key):    
                sum=0
                while(sum!=3):
                    if len(password)>8:
                        a=ucase(password)
                        b=ssymbol(password)
                        c=nnatural(password)
                        if a==b==c==1:
                            print("password saved")
                            sum=a+b+c
                        else:
                            password=input("password not secure\nenter password again")
                        
                    else:
                         password=input("string should be more than 8 character\nenter password again")
                
                path=fname+","+lname+","+un+","+password+","+"\n"
                f_write(path)
                if key==1:
                    credit="0"
                    debit="0"
                    balance="1000"
                    dv=credit+","+debit+","+balance+"\n"
                    un_data(un,dv)
                    print("Signup Succussfully")
def ssymbol(password):
                        b=['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@']
                        for i in password:
                            for j in b:
                                if i==j:
                                    return 1
def ucase(password):
                        
                        b=password.upper()
                        for i in password:
                            for j in b:
                                if i==j:
                                    return 1
def nnatural(password):
                        for i in range(49,58):
                            for j in password:
                                if chr(i)==j:
                                    return 1
                                
def signup():
            fname=input("enter your first name")
            lname=input("enter your last name")
            un=input("enter username")
            password=input("enter password")
            key=1
            password1(fname,lname,un,password,key)
def credit(amt,bcd,bun):
                        bb=bcd+amt
                        print("after credit amount is ",bb,"of",bun)
                        credit=amt
                        print("credit",credit)
                        credit=str(credit)
                        balance=str(bb)
                        bcf=credit+","+"0"+","+balance+"\n"
                        un_data(bun,bcf)
def debit(db,bcd,bun):
    if bcd>=db:
        bcd=bcd-db
        db=str(db)
        ame=str(bcd)
        print("remaining Balance",bcd,"of",bun)
        pp="0"+","+db+","+ame+","+"\n"
        un_data(bun,pp)
    else:
        print("debit amount is more than balance")
                 
option1=0
while(option1!=3):
    option1=int(input("press 1:: to signup\npress 2:: to login\npress 3:: Exit\n Enter option"))
    if option1==1:
        print("signup")
        signup()
    elif option1==2:
        lu,lp=[],[]
        fu=open("database.csv","r")
        d=fu.readlines()
        d.reverse()
        for line in d:
            line=line.split(",")
            lu.append(line[2])
            lp.append(line[3])
        bun=input("enter Username")
        if bun in lu:
            xx=lu.index(bun)
            bpas=input("enter password")
            if bpas==lp[xx]:
                option2=0
                while(option2!=6):
                    bcd=f_read(bun)
                    print("balance",bcd)
                    option2=int(input("Press 1 ::  Debit\npress 2 :: Credit\npress 3 :: Transfer\npress 4 :: Password Change\n press 5:: PassBook \npress 6:: Logout \nEnter Choice"))                
                    if option2==1:
                        db=int(input("debit option selected\n enter amount you want to debit"))
                        debit(db,bcd,bun)
                    elif option2==2:
                        amt=int(input("credit option selected \nEnter amount you want to add in account"))
                        credit(amt,bcd,bun)
                    elif option2==3:
                        print("bun",bun)
                        s_un=input("transfered option selected \n Enter username to whom you want to transfer")
                        if s_un in lu:
                            tam=int(input("username Found\n enter amount you want to transfer"))
                            fu=open(s_un+"1.csv","r")
                            r_b=fu.readlines()
                            for i in r_b:
                                i=i.split(",")
                                balance=i[2]
                                balance=eval(balance)
                                print("balance",bcd)
                            fu.close()
                            debit(tam,bcd,bun)
                            credit(tam,balance,s_un)
                    elif option2==4:
                        password=input("Change Password \nenter Password")
                        mgp=d[xx].split(",")
                        fname=mgp[0]
                        lname=mgp[1]
                        key=2
                        password1(fname,lname,bun,password,key)
                    elif option2==5:
                        key=1
                        databas=f_read(bun,key)
                        print("credit","debit","balance")
                        for i in databas:
                            d=i.split(",")
                            print(d[0],"\t",d[1],"\t",d[2])
                    elif option2==6:
                        print("logout")
                    else:
                        option2=input("wrong option\n enter choice again")
            fu.close()
    elif option1==3:
        print("exit")
    else:
        option1=int(input("wrong input try again\n enter 1 or 2 to repeat"))
