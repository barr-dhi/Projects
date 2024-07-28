import random
import json
class reserve():
    def __init__(self,cus_info,cus_bal):
      self.loc = {"tamilnadu":["madurai","chennai"],"andhrapradesh":["nellore","tirupati"],"karnataka":["bengaluru","mysuru"]}
      self.resbal = 10000000
      self.cus_info = cus_info
      self.cus_bal = cus_bal
          
class sbi(reserve):
    def __init__(self,cus_info,cus_bal):
      self.sbibal = 7500000
      super().__init__(cus_info,cus_bal)
      
class tamilnadu(sbi):
    def __init__(self,cus_info,cus_bal):
      self.tnbal = 5000000
      super().__init__(cus_info,cus_bal)

class karnataka(sbi):
    def __init__(self,cus_info,cus_bal):
      self.kabal = 5000000
      super().__init__(cus_info,cus_bal)
      
class andhrapradesh(sbi):
    def __init__(self,cus_info,cus_bal):
      self.apbal = 5000000
      super().__init__(cus_info,cus_bal)
      
class madurai(tamilnadu):
    def __init__(self,cus_info,cus_bal):
      self.mdubal = 2500000
      super().__init__(cus_info,cus_bal)
      
class chennai(tamilnadu):
    def __init__(self,cus_info,cus_bal):
      self.chebal = 2500000
      super().__init__(cus_info,cus_bal)

class nellore(andhrapradesh):
    def __init__(self,cus_info,cus_bal):
      self.nelbal = 2500000
      super().__init__(cus_info,cus_bal)
      
class tirupati(andhrapradesh):
    def __init__(self,cus_info,cus_bal):
      self.tirbal = 2500000
      super().__init__(cus_info,cus_bal)

class bengaluru(karnataka):
    def __init__(self,cus_info,cus_bal):
      self.benbal = 2500000
      super().__init__(cus_info,cus_bal)
      
class mysuru(karnataka):
    def __init__(self,cus_info,cus_bal):
      self.mysbal = 2500000
      super().__init__(cus_info,cus_bal)

class local(madurai,chennai,mysuru,bengaluru,nellore,tirupati):
    def __init__(self,cus_info,cus_bal):
       super().__init__(cus_info,cus_bal)
    
    def banksbal(self):
        b = self.cus_bal
        res = 0
        for sub in b.values():
            for key,val in sub.items():
                res += val
        print("reserve bank bal = ",self.resbal+res)
        print("SBI bal = ",self.sbibal+res)
        for acc,det in self.cus_info.items():
            if(det['City'] == 'chennai'):
                print("Chennaibal = ",self.chebal+self.cus_bal[acc]["balance"])
                self.tnbal += self.cus_bal[acc]["balance"]
            elif(det['City'] == 'madurai'):
                print("Madurai bal = ",self.mdubal+self.cus_bal[acc]["balance"])
                self.tnbal += self.cus_bal[acc]["balance"]
            elif(det['City'] == 'bengaluru'):
                print("Bengaluru bal = ",self.benbal+self.cus_bal[acc]["balance"])
                self.kabal += self.cus_bal[acc]["balance"]
            elif(det['City'] == 'mysuru'):
                print("Mysuru bal = ",self.mysbal + self.cus_bal[acc]["balance"])
                self.kabal += self.cus_bal[acc]["balance"]
            elif(det['City'] == 'tirupati'):
                print("Tirupati bal = ",self.mysbal + self.cus_bal[acc]["balance"])
                self.apbal += self.cus_bal[acc]["balance"]
            elif(det['City'] == 'nellore'):
                print("Nellore bal = ",self.mysbal + self.cus_bal[acc]["balance"])
                self.apbal += self.cus_bal[acc]["balance"]

        print("TamilNadu bal = ",self.tnbal)
        # print("Madurai bal = ",self.mdubal)
        # print("Chennaibal = ",self.chebal)
        print("AndhraPradesh bal = ",self.apbal)
        # print("Nellore bal = ",self.nelbal)
        # print("Tirupati bal = ",self.tirbal)
        print("Karnataka bal = ",self.kabal)
        # print("Mysuru bal = ",self.mysbal)
        # print("Bengaluru bal = ",self.benbal) 
        self.tnbal = 5000000
        self.kabal = 5000000
        self.apbal = 5000000 
         
    
    def bal(self,acc_no):
       print("Customer's Balance: ",self.cus_bal[acc_no]['balance']) 
       
    def open(self):
        acc_no = "5678" + str(random.randint(1000,9999))
        # acc_no = int(input("Enter account number: "))
        if acc_no in self.cus_info:
            cus.open()
        else:
            cus_name = input("Enter the customer name: ")
            cus_age = int(input("Enter your age: "))
            print("""select your city from options below:
                    1.madurai
                    2.chennai
                    3.mysuru
                    4.bengaluru
                    5.tirupati
                    6.nellore""")
            inp = int(input("option: "))
            if(inp == 1):
                cus_city = (self.loc["tamilnadu"][0])
            elif(inp == 2):
                cus_city = (self.loc["tamilnadu"][1])
            elif(inp == 3):
                cus_city = (self.loc["karnataka"][1])
            elif(inp == 4):
                cus_city = (self.loc["karnataka"][0])
            elif(inp == 5):
                cus_city = (self.loc["andhrapradesh"][1])
            elif(inp == 6):
                cus_city = (self.loc["andhrapradesh"][0])
            else: 
                print("please select options from only above please try again")
                cus.open()
            
            amt = 0
            self.cus_info[acc_no]={"Name":cus_name,"Age":cus_age,"City":cus_city}
            self.cus_bal[acc_no] = {"balance":amt}
            print("Account Created Successfully, Your Account number is: ",acc_no)
            
    def close(self,acc_no):
        if(self.cus_bal[acc_no]['balance']==0):
            print("Account Closed Successfully ",self.cus_info[acc_no]," is no more Available")
            del self.cus_info[acc_no]
            del self.cus_bal[acc_no]
        else:
            print("""Please withdraw your current balance to close your account.
                  your current Balance is: """,self.cus_bal[acc_no]['balance'])
            print("""would you like to withdraw your Balance?
                      1. Yes
                      2. No""")
            opt = int(input("Enter the option: "))
            if(opt==1):
                cus.debit(acc_no)
                cus.close(acc_no)
            else:
                exit
            
    def credit(self,acc_no):
        amt = int(input("Enter the amount to deposit: "))
        self.cus_bal[acc_no]['balance'] += amt
        print("amount credited successfully. current balance: ",self.cus_bal[acc_no]['balance'])
        
    def debit(self,acc_no):
        amt = int(input("Enter the amount to withdraw: "))
        if(amt<=self.cus_bal[acc_no]['balance']):
            self.cus_bal[acc_no]['balance'] -=amt
            print("amount debited successfully. current balance: ",self.cus_bal[acc_no]['balance'])
        else:
            print("Insufficient Balance,Your current Balance is: ",self.cus_bal[acc_no]['balance'])
            cus.debit(acc_no)

    def login(self):
        logintry=3
        while(logintry>0):
            acc_no = input("Enter your acc_no: ")
            if acc_no in self.cus_info:
                while(1):
                    print("""select your action below:
                        1.Deposit
                        2.Withdrawel
                        3.check Balance
                        4.acc_close
                        5.Exit""")
                    opt = int(input("option: "))
                    if(opt==1):
                        cus.credit(acc_no)
                    elif(opt==2):
                        cus.debit(acc_no)
                    elif(opt==3):
                        cus.bal(acc_no)
                    elif(opt==4):
                        cus.close(acc_no)
                    else:
                        break
                break    
            else:
                print("Account Not Found Try Again.")
                logintry-=1
                print("login Tries left: ",logintry)
    
    def action(self):
        while(1):
            print("""select your action below:
                1.open new account
                2.login
                3.view Existing customer Details
                4.overall banks Balance
                5.Exit""")
            opt = int(input("option: "))
            if(opt==1):
                cus.open()
            elif(opt==2):
                cus.login()
            elif(opt==3):
                print("available customers list : ",self.cus_info)
            elif(opt==4):
                cus.banksbal()
            else:
                break

rd = open("accounts.txt",'r')
det = rd.read()
d={}
if(det):
    de = json.loads(det)
    d.update(de)
    print("Data type after reconstruction : ", type(d)) 
    print(d)
rd.close()
    
rb = open("balance.txt",'r')
bal = rb.read()
b={}
if(bal):
    ba = json.loads(bal)
    b.update(ba)
    print(b)
rb.close()
          
cus = local(d,b)
cus.action()
print(cus.cus_info)
storedetails = open("accounts.txt",'w')
storebal = open("balance.txt",'w')
if(cus.cus_info):
    storedetails.write(json.dumps(cus.cus_info,indent=5))
    storebal.write(json.dumps(cus.cus_bal,indent=5))
storedetails.close()