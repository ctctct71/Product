
import json

def load_products() :
    with open ("products.json" , "r") as file :
        products = json.load(file)    
    return products
def save_products(products) :
    with open("products.json" , "w") as file :
        json.dump(products , file)  
        
def add_product() :
        products = load_products()
        while True :
            name = input("نام محصول جدید :")
            if name == "" :
                print("نام نمی تواند خالی باشد")
                continue
            break    
        while True :
            try :    
                stock = int(input("موجودی محصول جدید :"))
                if stock < 0 :
                    print("عدد نمی تواند منفی باشد ")
                    continue
                break
            except ValueError :
                print("لطفا فقط عدد وارد کنید !!!!!")
        while True :
            try :
                price = int(input("قیمت محصول جدید :"))
                if price < 0 :
                   print("عدد نمی تواند منفی باشد ")
                   continue
                break
            except ValueError :
                print("لطفا فقط عدد وارد کنید !!!!!")
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
            save_products(products)
            print("محصول با موفقیت اضافه شد")
def search_product() :
      products = load_products()           
      found = False
      while True :
          name = input("نام محصول را وارد کنید :")
          if name == "" :
              print("نام نمی تواند خالی باشد")
              continue
          break 
      for product in products :
          if name in product["name"]:
              print(f'نام محصول :{product["name"]} موجودی محصول :{product["stock"]} قیمت محصول :{product["price"]}')
              found = True
      if found == False :
          print("محصول یافت نشد.")
def change_price():
    products = load_products()
    found = False
    while True :    
        name = input("نام محصول را وارد کنید :")
        if name == "" :
                print("نام نمی تواند خالی باشد")
                continue
        break 
    while True :
        try :
            new_price = int(input("قیمت جدید را وارد کنید :"))
            if new_price < 0 :
                print("عدد نمی تواند منفی باشد ")
                continue
            break
        except ValueError :
            print("لطفا فقط عدد وارد کنید !!!!!")
    for product in products :
        if product["name"] == name :
            product["price"] = new_price
            found = True
            break
    if found :    
        save_products(products)
        print("قیمت تغییر یافت ")
    else :
        print("محصول یافت نشد")
def change_stock() :
    products = load_products()
    found = False 
    while True :
        name = input("نام محصول را وارد کنید :")
        if name == "" :
                print("نام نمی تواند خالی باشد")
                continue
        break 
    while True :
        try :    
            new_stock = int(input("موجودی جدید را وارد کنید :"))
            if new_stock < 0 :
                print("عدد نمی تواند منفی باشد ")
                continue
            break
        except ValueError :
            print("لطفا فقط عدد وارد کنید !!!!!")
    for product in products :
        if product["name"] == name :
            product["stock"] = new_stock
            found = True
            break
    if found :        
        save_products(products)
        print("موجودی تغییر یافت ")
    else :
        print("محصول یافت نشد")
def remove_product() :
    products = load_products()
    found = False
    while True :    
        name = input("نام محصول را وارد کنید :")
        if name == "" :
            print("نام نمی تواند خالی باشد")
            continue
        break     
    for product in products :
        if product["name"] == name :
            products.remove(product)
            found = True
            break
    if found :    
        save_products(products) 
        print("محصول با موفقیت حذف شد")    
    else :
        print("محصول یافت نشد") 
def buy_product() :
    products = load_products()
    name = input("نام محصول را وارد کنید :")
    while True :
        try :
            count = int((input("تعداد خرید محصول :")))
            if count <= 0 :
                print("تعداد خرید باید بیشتر از صفر باشد")
                continue
            break
        except ValueError :
            print("لطفا فقط عدد وارد کنید !!!!!")
    found = False
    for product in products :
        if product["name"] == name :
            found = True
            if product["stock"] >= count :
                total_price = product["price"] * count
                print("خرید محصول با موفقیت انجام شد")
                print(f'قیمت هر عدد : {product["price"]}')
                print(f'تعداد خرید : {count}')
                print(f'مبلغ کل : {total_price}')
                product["stock"] -= count
                print(f'موجودی جدید : {product["stock"]}')  
                save_products(products)
            else :
                print(" موجودی کافی نمی باشد ")
            break    
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
    print("7. نمایش محصولات ناموجود")
    print("8. خرید محصول")
    print("9. ارزش خرید محصولات")
    print("10. گران ترین محصول")
    print("11. ارزانترین محصول")
    print("12. نمایش محصولات بر اساس قیمت از ارزان به گران")
    print("13. فیلتر کردن محصولات")
    print("13. خروج")
    try :
        choice = int(input("لطفا عدد موردنظر را وارد کنید: ")) 
    except ValueError :
        print("لطفا فقط عدد وارد کنید !!!!!")
        continue
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
        products = load_products()
        for product in products :
            print(f'{product["name"]} --> {product["stock"]} , {product["price"]}')
    elif choice == 7 :
        print("نمایش محصولات ناموجود")
        found = False
        products = load_products()
        for product in products :
            if product["stock"] == 0 :
                print(f'{product["name"]} --> {product["price"]}')
                found = True
        if found == False :
                print("هیچ محصول ناموجودی وجود ندارد")
    elif choice == 8 :
        print("خرید محصول")     
        buy_product()
    elif choice == 9 :
        print("ارزش خرید محصولات")
        products = load_products()
        total = 0
        for product in products :
            arzesh = product["price"] * product["stock"]
            total += arzesh
        print(f" ارزش کل موجودی : {total}")
    elif choice == 10 :
        products = load_products()
        max_price = 0
        max_product =""
        for product in products :
            if product["price"] > max_price : 
                max_price = product["price"]
                max_product = product["name"]
        print(f"گران ترین محصول : {max_product}")
        print(f"قیمت گرانترین محصول : {max_price}")
    elif choice == 11 :
        print("ارزانترین محصول")
        products = load_products()
        min_price = products[0]["price"]
        min_product = products[0]["name"]
        for product in products :
            if product["price"] < min_price : 
                min_price = product["price"]
                min_product = product["name"]
        print(f"ارزان ترین محصول : {min_product}")
        print(f"قیمت ارزان ترین محصول : {min_price}")
    elif choice == 12 :
        print("نمایش محصولات بر اساس قیمت از ارزان به گران")
        products = load_products()
        sorted_products = sorted(products , key=lambda product: product["price"])
        for product in sorted_products :
            print(f' نام محصول :{product["name"]} -->  قیمت محصول : {product["price"]}')    
    elif choice == 13 :
        print("فیلتر کردن محصولات")
        products = load_products()
        for product in products :
            if product["stock"] < 5 :
                print(f'{product["name"]} --> {product["stock"]}')
    elif choice == 14 :
        print("خروج از برنامه...")
        break
    else:
        print("گزینه نامعتبر است!")
        

