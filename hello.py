print ("hello world")
print ("123123")
message = "hello world"
print (message)
name = "amirali akhondi"
print (name.title())    
print (name.upper())
print (name.lower())
print("merc mamnooooooon")
firstname = "amirali"
lastname = "akhondi"    
fullname = f"{firstname}-{lastname}"
print(f"Hello ,I'm {fullname.title()}!")
message = f"Hello, I'm {fullname.title()}!"
print(message)
print("\t python")
print(f" hi again \n I'm {fullname.title()} \n bye")
a = "amirali "
a.rstrip()
print (a)
b = "   amirali    "
b.strip()
print(b)
print (6/2)
a , b , c = 1,2,3
print(b)
a = ['bg','jh','sdf','sdfer','qeqweqwe','sdwqe2']
print(a[3].title(),a[5].upper())
print(a[-1].lower())
mes = f"this is my first list : {a[-1].title()}, {a[0].upper()}, {a[3].lower()}, {a[1].strip()}"
print(mes)  
a[1] = 'vaji'
print(a)
a.append('amirali') , a.append('gty')   
print (a)
a.insert(0,'bghg'), a.insert(3,'sdfgdfdf'),a.insert(5,'sdfewewe')   
print(a)
a.remove('amirali') , a.remove('sdfgdfdf')  # faghat baraye hazf kardan item ha be kar mire
print(a)
del a[0] 
print(a)
a.pop() #baraye inke akharin item ro hazf kone va  index ro ham neshon bede
print(a)
a.pop(2)
print(a)
a.append('amirali') , a.append('gty')
print (a)
a.pop()
print(a)
print (f" \nA sdfdf")
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati'] 
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")
motorcycles.sort(reverse=True) # baraye inke list asli ro sort kone ro asli list taghir mide
print(motorcycles)
print(sorted(motorcycles))   # baraye inke sort shode ro neshon bede vali list asli ro taghir nade
print(motorcycles.reverse()) 
len(motorcycles) # baraye inke tedad item ha ro neshon bede
print(len(motorcycles))    
c = ['ksdf', 'sdfsdf', 'sfgthth']
for item in c : # baraye inke har item ro dar list check kone   
    print(item.title())
for n in c : 
    print(f"this is my list : {n.upper()}")
for i in range( 1,6):
    print(i)
numbers = list(range(1,10,2))
print(numbers)
squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)  
    print(squares)        
min(numbers) # baraye inke kamtarin item ro neshon bede
max(numbers) # baraye inke bishtarin item ro neshon bede
sum(numbers) # baraye inke majmoe item ha ro neshon bede
squares = [value ** 2 for value in range(1,11)] # baraye inke square item ha ro neshon bede    LIST COMPREHENSION
result =[]
for i in numbers:
    result.append(i**2)
print(result)
result = [i**2 for i in numbers]
print(result)   
asdf =[]
for i in numbers :
    asdf.append(i+ 10)
print(asdf)  
asdf = [i+10 for i in numbers]  
print(asdf)
square = [i**2 for i in range(1,6)]
print(square)
print(motorcycles[0:2])
print(motorcycles[:3])
print(motorcycles[2:])
print(motorcycles[-2:])    # 2 taye akhare list ro neshoon mide  motorcycles[-2] yani yeki monde b akhar 
motorcycles.append ("benz") , motorcycles.append("bmw") , motorcycles.append('reno')
print(motorcycles)
for i in motorcycles[:3] :
    print(i.title())
stu = motorcycles [:]
print (stu)    
stu.append ("kmc")
print(stu)
print(motorcycles)
motorcycles.insert(4,"toyota") #ezafe kardan dar jaye moshakhas
print(motorcycles)
print(numbers)
h = [2,4,6,8]
numbers.extend(h)    #ezafe kardan chand ta 
print(numbers)
print(len (numbers))
print(len(motorcycles))
print("kmc" in motorcycles)
print(motorcycles.index("bmw"))
print(numbers.count(2))  #tedad tekrar ye adad
adad = [1,24,6543,4,5,6]
adad.sort()
print(adad)
adad.clear
adad_new = sorted(adad) #sort shode jadid misazad
print(adad)
print(adad_new)
print(stu)
for i ,n in enumerate(stu) :   #ham index ham value
    print(i,n)
resulsdfsfd = [x *3 for x in adad if x % 2 == 0] 
print(resulsdfsfd)   
a = [1,2]
b = a
a.append(3)
print(b)
b = a.copy()
print(b)
n = [["ali" , 18] , ["sd", 21 ], ["jh",23]]
print(n[2][0])
s = (1,3,4)
print(s) 
car = "bmw"
if  car.upper() != "BMW" :
    print ("a")
else:
    print ("hichi")    
a = ["as","sdf","wee","sgg","dsf"]
if "sdf" in a :
    print (f"{a[2]}, ok!!")
nb = "sx"
sdfsdfff = ["eyval"] if "sx" in nb and len(nb) == 2 else []     #value_if_true if condition else value_if_false
print(sdfsdfff)
names = ["ali"]
if names :    #baresi khali boodan list 
    print("sdf")
o = ("m" , "n" , 1)    
if len(o) > 4 :
    print("yes")
elif o[1] == "p" :
    print("no")
elif o[2] == 1 :
    print("ok")     
else :   
    print ("yyyy")    
score = 16
if score >= 18 and score <= 20 :
    print("exellent")
elif score >= 15 and score <= 17 : 
    print ("good")
elif score >= 10 and score <= 14  :
    print("pass")
elif score >= 0 and score <= 9 :
    print ("fail")             
age = 25
if age < 13 :
    print ("child")
elif age >= 13 and age <= 17 :
    print("teenager")
elif age >= 18 and age <= 60 :
    print("adult")
elif age > 60 :
    print("senior")    
mn = ["gh", "fdfdf", "hhhh","tttt", "yyy"]
ser = ["sdfsfasdfasfd" , "dferttrt"]
for i in mn :
    if ser in mn :
        print(f"it's ok man in ser") 
    else :
        print("coool") 
bb = {"ali": 2, "reza": 3, "jjj":1}
print(bb["ali"])
new_bb = bb["jjj"] 
print(f"ez sd {new_bb}")
bb ["fdfdf"] = 33      #ezafe kardan b dictionary
print(bb)
alien = {'x_position': 0 , 'y_position': 25 , 'speed':'medium'}
print(f"orginal position : {alien["x_position"]}")
if alien['speed'] == 'slow' :
    gh_gh = 1
elif alien['speed'] =='medium' :
    gh_gh = 2    
else : 
    gh_gh = 3
alien['x_position'] += gh_gh
print(f"new_position : {alien['x_position']}")  
del bb["fdfdf"]
print(bb)    
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'}
language = favorite_languages['sarah'].title()    
print(f"sarah's favorite language is {language}")
print(bb.values())
print(bb.items())
print(bb.get("ali"))
bb.pop("ali")                   #pak mishe
bb.popitem()                    # akhari pak mishe
ha = {"je" : 12 , "df" : 32 , "hh" : 54 , "tyy": 44}
for keys , values in ha.items() :
    if values > 10 :
        print(f"this persons are {keys} and numbers {values}")
k = {'ali' : 'red' }
m = {'ber' : 'white'}
l = {'tre' : 'blue'}
kml = [k,m,l]
kml.append("j")
print(kml)
oly = []
for i in range(5) :
    new_oly = [{"fgh" : 12 , "jkl" : 13 , "yhb" : 14}]
    oly.append(new_oly)
print(f"\t + oly")
f =  { "c" : [1 , "ty"], "h": [2 , "rs"], "u" :[5, "io"]}      #list dar dictionary
for i,s in f.items() :
    print(f"\n {i.title()} is here ")
    for m in s :
        print(f"\t{m}")

k ={
    "tim" : {"firstname" : "timber" , "lastname" : "saw" , "sen" : 15},
    "drow" : {"firstname" : " drow" , "lastname" : "ranger" , "sen" : 14},
    "phantom" : {"firstname" : "phantom" ,"lastname" : "lancer" , "sen" : 26}
}
for name , bio in k.items():
    if name == "klinz" :
        print("nothing is here")
    elif bio["sen"] == 15 :
        print(f"\n {bio["sen"]} hastesh")
lk = input("ye shomare begoo : ")
lk= int(lk)
if lk % 2 == 0 :
    print(f"\n {lk} zoje k! ")
else :
    print(f"\t pas {lk} farde! ")    

prompt = "\n tell me something , and i will repeat it back to you :"
prompt += "\n enter 'quit' to end the program . "
active = True
while active :
    mess = input(prompt)
    if mess == 'quit':
        active = False
    else :
        print(mess)    
while active : 
    see = input(prompt)
    if see == 'quit' :
        break
    else :
        print(f"no this {prompt.title}")    
password = ""
while password != "1234" :
    password = input("password : ")
    print("doroste!")    

while True :
    number = int(input("ye shomare begoo"))
    if number == 0  :
        break     #halghe ro motevaghef mikone
    print(number)

x = 0
while x < 10:
    x = int(input("begoo: "))
    x += 1
    if x == 5:
        continue             #halghe ro rad mikone mire badi 
    print(x)
    break

x = 0
while True :
    x = int(input("begoo :"))
    if x % 2 == 0 :
        continue    
    print(x)
   
x = 10
while x < 12 :
     print (x) 
     x += 1 
else :                      # akhare shart bade az in k while tamoom mishe else ejra mishavad     
    print("finish")         # break bashe motevaghef mishavad shart va else ham ejra nemishe

counter = 0
while counter < 10 :
    print("hi") 
    counter += 1

counter = 0
number = 1
while number < 5 :
    counter += number 
    number += 1
print(counter)

total = 0
while True:
    number = int(input("shomare :"))
    if number == 0:
        break
    total += number
print("jam:", total)

number = 0
while number <= 10 :
    print(number)
    number += 1

number = 0
while number <= 20 :
    if number % 2 ==0 :
        print(number)
    number += 1 

total = 0
counter = 0 
while True :
    number = int(input("shomare bede :"))
    if number == 0 :
        break
    counter += 1
    total += number
print(total)    
print(counter)

while True :
    ramz = int(input("ramz bede :"))
    if ramz == 1234 :
        print("dorste") 
        break

count = 0
counter = 0
while True:
    number = int(input("shomare bede :"))
    if number == 0:
        break
    if number % 2 == 0:
        count += 1
    else:
        counter += 1
print("زوج:", count)
print("فرد:", counter)

def greet_user(username) :
    print(f"im amirali , {username.title()}!")
greet_user("amirali")

def jam(a,b) :
    print(a+b)
jam(1,2) 

def menha(a,b,c) :
    return a - b - c 
result = menha(10,3,3)
print(result)

def show_name(name ="ali") :
    print("hi", name)
show_name()  
show_name("amirali")        

def add(*numbers): #nemidoonim chand ta meghdar mikhaym ezafe konim
    print(numbers)
add(1,2,3,4,5,6,7)    

def add(*numbers):
    total = 0
    for i in numbers :
        total += i
    return total 
print(add(1,10,20,30))   

def person(**info):
    print(info)
person(name = "ali" , age = 20 , city = "tehran")
print(person())    


def get_number() :
    number = int(input("shomare bede :"))
    return number
number = get_number()
print(number)

def check_number(number):
    if number > 0 :
        return "mosbat"
    elif number < 0 :
        return "manfi"
    else :
        return "sefr"
print(check_number(-10))    

def get_number() :
    total = 0
    while True :
        number = int(input("shomare begoo :"))
        if number == 0 :
            break 
        total += number
    return total
result = get_number()
print(result , "jamesh shod in ")

def test():
    number = 10
print(number())  #error mide chon number dakhle function teste

def jam(a,b):
    return a + b
def zarb (jam , c) :
    return jam * c
zarb(jam(1,2),4)

def salam(name , age) :
    print(f"salam {name} ,sen :{age}")
salam("amir" , 25)    

def jam(a,b):
    return  a + b 
result = jam(10,20)
print(result)

def tafrigh(a,b):
    return a - b 
result = tafrigh(4, 3)
print(result)

def mosavi(a,b):
    if a == b :
        return "barabar"
    else :
        return "barabar nist "
    
def zoj_fard(a) :
    if a % 2 ==0 :
        return "zoj"
    else :
        return "fard"
    
def salam() :
    name = input("esm begoo : ")
    return f"salam {name}"    
salam()    

def masahat(tool,arz) :
    return tool * arz
masahat(4,5)

def calculator(a,b,amal) :
    if amal == "+" :
        return a + b
    elif amal == "-" :
        return  a - b
    elif amal == "*" :
        return a * b
    elif amal == "/" :
        return a / b 
    else :
        return "amal nadorost hast "
print(calculator(1 , 3 , "*"))   

def salam (name ="Amir"):
    return name 
print(salam())

def information(name , age , city ) :
    return f"{name} - {age} -{city} "
print(information(age=25, city="tehran", name="ali"))   

def factor(name,tedad,gheymat) : 
    total= tedad * gheymat
    return f"{name} : {total}"
print(factor("pen", 12, 500))

def hesab(name, gheymat, tedad=1):
    kol = tedad * gheymat

    if kol > 100000:
        return f"{name} - {kol} - geroon"
    else:
        return f"{name} - {kol} - monaseb"

print(hesab("laptop", 60000, 2))

def max_number (*args):
    max_num = args[0]
    for i in args :
        if i > max_num :
            max_num = i
    return max_num
print(max_number(1,2,3,4))

def jam_number (*args):
    total = 0
    for i in args :
        total += i 
    return total   
print(jam_number(10,20,5,15))    

def information(**kwargs) :
    for key , value in kwargs.items() :
        print(f" {key} : {value}")
print(information(name = "amir" , age = 25 , city = "tehran"))

def moshakhasat(**kwargs) :
    count = 0
    for  key, value in kwargs.items():
       count += 1
    return count
print(moshakhasat(name ="amir" , age = 25 , city = "tehran"))    

def moshakhasat (**kwargs) :
    for key , value in kwargs.items() :
        if  isinstance(value, (int, float)) :  
            print( f"{key} : {value}" )
print(moshakhasat(name = "amir" , age = 25 , city ="tehran", score = 18))        

def moshakhasat (**kwargs) :
    total = 0
    for key , value in kwargs.items():
        if  isinstance(value, (int, float)) :
            total += value
    return total       
print(moshakhasat(name="amir", age=25, city="tehran", score=18, height=180)) 

def top_number(**kwargs) :
    top = 0
    for key,value in kwargs.items() :
        if  isinstance(value, (int, float)) and value > top :
            top = value
    return top
print(top_number(name="amir", age=25, city="tehran", score=18, height=180))    
            
def count_number(**kwargs) :
    count = 0
    for  key, value in kwargs.items():
       if  isinstance(value, (int, float)) :
        count += 1
    return count
print(count_number(name="amir", age=25, city="tehran", score=18, height=180)) 

def info(*args , **kwargs) :
    total = 0
    count = 0
    for i  in args :
        total += i
    for key , value in kwargs.items() :
        if isinstance(value, (int , float)) :
            count += 1 
    return (f"مجمع args : {total}   ,تعداد اعداد kwargs: {count}")       
print(info(10, 20, 30, name="amir", age=25, score=18, city="tehran"))    

def forosh (*args , **kwargs) :
    count = 0
    total = 0
    for i in args :
        total += i
      
    for key , value in kwargs.items() :
        if isinstance(value,(int , float )) :
            count += 1
    if total > 100000 :
          status = ("گران")
    else :
          status = ("مناسب")        
    return (f"مجموع : {total} \n تعداد اطلاعات عددی :{count} \n وضعیت : {status} " )       
print(forosh(30000, 25000, 60000,name="amir",age=25,city="tehran",code=123)) 

class person:
    def __init__(self , name , age , city) :
        self.name = name
        self.age =age 
        self. city = city
person1 = person("ali", 25 ,"tehran")        
print(person1.name)        
print(person1.age)
print(person1.city)


class person :
    def __init__(self , name , age) :
        self.name = name 
        self.age = age 
    def salam(self) : 
        print(f"salam , man {self.name} hastam")
person1 = person("ali", 25)
person1.salam()

class calculator :
    def __init__(self , number) :
        self.number = number
    def add(self , value ) :
        return self.number + value
calc = calculator(10)    
print(calc.add(5))

class Product :
    def __init__(self , name , price , count) :
        self.name = name 
        self.price = price 
        self.count = count
    def total_price(self) :
        return self.price * self.count
product1 = Product("laptop", 60000, 2) 
print(product1.name)
print(product1.total_price())   

donations = {'jadi' : 20 , 'sara' : 800 , 'far' :12 , 'hasan' : 9}
def donation_analysis(don) :
    person = ''
    total = 0
    count = 0
    max_donation = -1
    for name , value in don.items() :
        total += value
        count += 1
        if value > max_donation:
            person = name
            max_donation = value
        average = int((total/count))
    return average , total , person
avg , total , max_person = donation_analysis(donations) 
print(f" total donatoions : {total}")
print(f" average donation is {avg}")
print(f" thanks to {max_person}")

class Person :                                                                  # Class: Person
      def __init__(self , age , name , city) :                                  #        │
           self.name = name                                                     #        ├── person1
           self.age = age                                                       #        │     ├── name = ali
           self.city =city                                                      #        │     ├── age = 15
      def information(self) :                                                   #        │     └── city = tehran
           return f" {self.name} , {self.age} , {self.city}"                    #        │ 
      def change_Age(self, new_age) :                                           #        └── person2 
           self.age = new_age                                                   #              ├── name = reza
           return f" {new_age} sene jadide "                                    #              ├── age = 30
      def change_city(self,new_city) :                                          #              └── city = shiraz
           self.city = new_city
      def age_next_year (self) :
           return self.age + 1 
      def is_adult (self) :
           if self.age >= 18 :
               return f" bozorge ! "
           else :
               return f" bozorg nist"       
      def age_group(self) :
           if self.age < 13 :
                return f"کودک"
           elif self.age <= 17 :
                return f"نوجوان"
           elif self.age < 60 :
                return f"بزگسال"
           else :
                return f"سالمند"                                                  
person1 = Person(15, "ali", "tehran")                                           
print(person1.age)                                                              
person2 = Person(30 ,"reza", "shiraz")                                         
print(person2.name)                                                            
print(person2.age)
print(person2.city)
print(person2.information())      
person2.age = 31                                                               
print(person2.age)
print(person2.information())  
print(person2.change_Age(32))    
print(person2.age)
person2.change_city("mashhad")
print(person2.city)
print(person2.age_next_year())
print(person2.is_adult())
person1 = Person(10, "ali", "tehran")
person2 = Person(16, "reza", "shiraz")
person3 = Person(30, "amir", "tabriz")
person4 = Person(65, "hasan", "mashhad")

print(person1.age_group())
print(person2.age_group())
print(person3.age_group())
print(person4.age_group())

class Car :
    def __init__(self, brand , model , year ):
        self.brand = brand
        self.model = model
        self.year = year
    def information(self) :
        return f" my car is {self.brand} , { self.model} , {self.year}"
    def car_age(self) :
        car_age = 2026 - self.year
        return car_age
    def is_new(self) :
        if self.car_age()<=5:
            return f"ماشین نسبتا جدید است"
        else :
            return f"ماشین قدیمی است "
car1 =Car("toyota", "camry", 1992)         
car2 =Car("benz", "c200", 2000)
print(car1.year)
print(car1.car_age()) 
print(car1.is_new())
                       
class BankAccount :
    def __init__(self, owner , balance , account_number):
        self.owner = owner
        self.balance = balance
        self.account_number = account_number
    def show_balance(self) :
        return f" total balance = {self.balance}"
    def deposit(self,amount) :
       self.balance += amount
       return self.balance
    def withdraw(self,amount) :
        if self.balance >= amount :
          self.balance -= amount
          return self.balance
        else :
            return f"موجودی کافی نیست !"    
    def account_info(self) :
        return f" صاحب حساب : {self.owner} \n شماره حساب : {self.account_number} \n موجودی : {self.balance}"
account1 = BankAccount("Ali", 5000000, "12345")
print(account1.show_balance())
print(account1.deposit(2000000))
print(account1.withdraw(3000000))
print(account1.account_info())    

class Product :
    company = "tech store"
    tax = 0.09
    def __init__(self,name, price , stock) :
        if price < 0 :
            raise ValueError ("قیمت نمیتواند منفی باشد")
        if stock < 0 :
            raise ValueError ("موجودی نمیتواند منفی باشد ")
        
        self.name = name
        self.price = price
        self.stock = stock
    def show_info(self) :
        return f" نام کالا : {self.name} \n قیمت : {self.price} \n موجودی : {self.stock}"
    def sell(self , quantity) :
        if self.stock >= quantity :
            self.stock -= quantity
            total = self.price * quantity
            return  total , self.stock
        else :
            return f"موجودی حساب کافی نمی باشد !"
    def add_stock(self , quantity) :
        self.stock += quantity
    def discount(self , percent):
      self.price = self.price - (self.price * percent / 100)
      return  self.price
    def price_with_tax(self) :
        return self.price + (self.price * Product.tax)       
product1 = Product("Laptop", 50000000, 10)
print(product1.show_info())
print(product1.sell(3))
print(product1.show_info())
product1.add_stock(5)
print(product1.show_info())
print(product1.discount(20))    
print(product1.company)  
product1.company = "Amazon"
print(product1.company)                                                   
print(product1.price_with_tax())                                                                                
                                                                                
try :
        a = float(input("adad vared konid ?"))
        b = float(input("adad vared konid ?"))
        result = a / b
        print((result))
except ValueError :
        print("adad vared konid ! ")
except ZeroDivisionError :
        print("taghsim nemishavad !")
        
try :                                                                          
    a =float(input("add ra varde konid ?"))
    print(a)
except  ValueError :
    print ("adade sahih vared kon")    

try :
    age = int(input("sen begoo"))
    print(a)
except ValueError :
    print("sen besoorate adad vared konid !")
else :
    if age < 18 :
        print("shoma zire 18 sal hastid ")
    elif age >= 18 :
        print("shoma bozorgsal hastid")
    
# try:
    # تلاش برای اجرای کد

# except:
    # مدیریت خطا

# else:
    # اگر خطایی نبود

# finally:
    # در هر صورت    

import json 
product = {
    "name" : "amirali" ,
    "price" : 2500 ,
    "stock" : 4}
with open("product.json", "w") as file :
    json.dump(product,file)
    
with open("product.json" ,"r") as file :
    product = json.load(file)
print(product)
print(product["name"])    
print(product["price"])
print(product["stock"])    

product = {
    "name" : "amirali" ,
    "price" : 2500 ,
    "stock" : 4}
with open ("product.json", "w") as file :
    json.dump(product,file)
product = {
    "name" : "amirali" ,
    "price" : 3000 ,
    "stock" : 10}
with open("product.json" , "w") as file :
    json.dump(product, file) 
with open ("product.json", "r") as file :
    product = json.load(file)
print (product)    
    
products = [
    {"name": "Laptop", "price": 50000000, "stock": 10},
    {"name": "Mouse", "price": 500000, "stock": 20},
    {"name": "Keyboard", "price": 1000000, "stock": 15}
]
with open("products.json", "w") as file :
    json.dump(products, file)
for product in products :
    if product["name"] == "Mouse" :
        product["price"] = 600000 
with open("products.json", "w") as file :
    json.dump(products, file)
with open ("products.json" , "r") as file :
    products = json.load (file)
print(products)    

found = False
products = [
    {"name": "Laptop", "price": 50000000, "stock": 10},
    {"name": "Mouse", "price": 500000, "stock": 20},
    {"name": "Keyboard", "price": 1000000, "stock": 15}
]
with open("products.json" , "w") as file :
    json.dump(products,file)
product_name = input("نام محصول را وارد کنید:")        
new_price = int(input("قیمت جدید را وارد کنید:"))       
for product in products :
    if product["name"] == product_name :
        product["price"] = new_price
        found = True
if found == False :
    print("محصول پیدا نشد !")         
with open ("products.json" , "w") as file :
    json.dump(products,file)
with open ("products.json" , "r") as file :
    products = json.load(file)
print(products)        

import json

found = False
valid_price = True

products = [
    {"name": "Laptop", "price": 50000000, "stock": 10},
    {"name": "Mouse", "price": 500000, "stock": 20},
    {"name": "Keyboard", "price": 1000000, "stock": 15}
]

with open("products.json", "w") as file:
    json.dump(products, file)

product_name = input("نام محصول را وارد کنید: ")

try:
    new_price = int(input("قیمت جدید را وارد کنید: "))
except ValueError:
    print("لطفاً قیمت را به صورت عدد وارد کنید!")
    valid_price = False

if valid_price:
    for product in products:
        if product["name"] == product_name:
            product["price"] = new_price
            found = True

    if found == False:
        print("محصول پیدا نشد!")

    with open("products.json", "w") as file:
        json.dump(products, file)

with open("products.json", "r") as file:
    products = json.load(file)

print(products)

import json
product = {
    "name" : "Mouse" ,
    "price" : 50000 ,
    "stock" : 20
    }
data = json.dumps(product)
print(data)
print(type(data))
data = json.loads(data)
print(data)
print(type(data))

import json
products = [
    {"name": "Laptop", "price": 50000000, "stock": 10},
    {"name": "Mouse", "price": 500000, "stock": 20},
    {"name": "Keyboard", "price": 1000000, "stock": 15},
    {"name": "Monitor", "price": 8000000, "stock": 5}
]
found = False
data = json.dumps(products)
products = json.loads(data)
price_limit = int(input(" یک قیمت بگو :"))
for product in products :
    if product["price"] > price_limit :
        print(f'{product["name"]} --> {product["price"]}' )
        found = True
if found == False :        
    print("محصولی یافت نشد !")

import json
with open ("products.json" , "r") as file :
    products = json.load(file) 
name = input("نام محصول :")
price = int(input("قیمت : "))
stock = int(input("تعداد : "))
new_product = {
    "name" : name ,
    "price" : price ,
    "stock" : stock
    } 
found = False   
for product in products :
    if product["name"] == name :
        found = True
if found :
    print(" این محصول قبلا وجود دارد ") 
else : 
    products.append(new_product)
    with open("products.json", "w") as file :
        json.dump(products , file)
    print("محصول با موفقیت اضافه شد ! ")    
print(products)    

import json
with open("products.json", "r") as file:
    products = json.load(file)
name = input("نام محصول را وارد کنید: ")
found = False
for product in products:
    if product["name"] == name:
        print(f'نام: {product["name"]}')
        print(f'قیمت: {product["price"]}')
        print(f'موجودی: {product["stock"]}')
        found = True
if found == False:
    print("محصول پیدا نشد!")
    
import json
with open ("products.json" , "r") as file :
    products = json.load(file)
name = input("نام محصول را وارد کنید :")
new_price = int(input("قیمت جدید را وارد کنید :")) 
found = False
for product in products:
    if product["name"] == name:
        product["price"] = new_price
        found = True

if found: 
    with open("products.json", "w") as file:
               json.dump(products, file)
    print("قیمت با موفقیت تغییر کرد !")
else :
    print("محصول پیدا نشد !")           
    
import json
with open ("products.json" , "r") as file :
    products = json.load(file)
name = input("نام محصول را وارد کنید :")
new_stock = int(input("موجودی جدید را وارد کنید :")) 
found = False
for product in products:
    if product["name"] == name:
        product["stock"] = new_stock
        found = True

if found: 
    with open("products.json", "w") as file:
               json.dump(products, file)
    print("موجودی با موفقیت تغییر کرد !")
else :
    print("محصول پیدا نشد !")         

import json
with open("products.json" , "r") as file :
    products = json.load(file)
name = input("نام محصول را وارد کنید :")
found = False
for product in products :
    if product["name"] == name :
        products.remove(product)
        found = True
        break
if found: 
    with open("products.json", "w") as file:
               json.dump(products, file)
    print("محصول با موفقیت حذف شد !")
else :
    print("محصول پیدا نشد !")   

import json

def add_product() :
        with open ("products.json" , "r") as file :
            products = json.load(file)
        name = input("نام محصول جدید :")    
        stock = int(input("موجودی محصول جدید :"))
        price = int(input("قیمت محصول جدید :"))
        found = False
        new_product = { "name" : name ,
                       "stock" : stock,
                       "price" : price}
        for product in products :
            if product["name"] == name :
                found = True
        if found :        
                print("این محصول قبلا وجود دارد")
        else :
            products.append(new_product)
            with open("products.json" , "w") as file :
                json.dump(products , file)
            print("محصول با موفقیت اضافه شد")
def search_product() :
      with open ("products.json" , "r") as file :
          products = json.load(file)            
      found = False
      name = input("نام محصول را وارد کنید :")
      for product in products :
          if product["name"] == name :
              print(f'نام محصول :{product["name"]} موجودی محصول :{product["stock"]} قیمت محصول :{product["price"]}')
              found = True
      if found == False :
          print("محصول یافت نشد.")
def change_price():
    with open ("products.json" , "r") as file :
        products = json.load(file)
    found = False    
    name = input("نام محصول را وارد کنید :")    
    new_price = int(input("قیمت جدید را وارد کنید :"))
    for product in products :
        if product["name"] == name :
            product["price"] = new_price
            found = True
            break
    if found :    
        with open("products.json" , "w") as file :
            json.dump(products,file)
        print("قیمت تغییر یافت ")
    else :
        print("محصول یافت نشد")
def change_stock() :
    with open ("products.json" , "r") as file :
        products = json.load(file)
    found = False 
    name = input("نام محصول را وارد کنید :")    
    new_stock = int(input("موجودی جدید را وارد کنید :"))
    for product in products :
        if product["name"] == name :
            product["stock"] = new_stock
            found = True
            break
    if found :        
        with open("products.json" , "w") as file :
            json.dump(products,file)
        print("موجودی تغییر یافت ")
    else :
        print("محصول یافت نشد")
def remove_product() :
    with open ("products.json" , "r") as file :
        products = json.load(file) 
    found = False    
    name = input("نام محصول را وارد کنید :")    
    for product in products :
        if product["name"] == name :
            products.remove(product)
            found = True
            break
    if found :    
        with open("products.json" , "w") as file :
            json.dump(products , file)  
        print("محصول با موفقیت حذف شد")    
    if found == False :
        print("محصول یافت نشد") 

while True:
    print("------- مدیریت محصول --------")
    print("1. افزودن محصول")
    print("2. جستجوی محصول")
    print("3. تغییر قیمت")
    print("4. تغییر موجودی")
    print("5. حذف محصول")
    print("6. نمایش همه محصولات")
    print("7. خروج")

    choice = int(input("لطفا عدد موردنظر را وارد کنید: "))        
    if choice == 1:
        print("1. افزودن محصول")
        add_product()
    elif choice == 2:
        print("2. جستجوی محصول")
        search_product()
    elif choice == 3:
        print("3. تغییر قیمت")
        change_price()
    elif choice == 4:
        print("4. تغییر موجودی")
        change_stock()
    elif choice == 5:
        print("5. حذف محصول")
        remove_product()
    elif choice == 6:
        print("6. نمایش همه محصولات")
        with open("products.json" , "r") as file :
            products = json.load(file)
        for product in products :
            print(f'{product["name"]} --> {product["stock"]} , {product["price"]}')
    elif choice == 7:
        print("خروج از برنامه...")
        break
    else:
        print("گزینه نامعتبر است!")


