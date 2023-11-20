with open("data.txt","w") as file:
    file.write("你好嗎\n")
    file.write("71188\n")
    file.write("buerkj")

#%%
with open("data1.txt") as file:
    data=file.read()
    print(data)
#%%
import calendar
print(calendar.month(2019,1))


import calendar as cal
print(cal.month(2019,2))

from calendar import month
print(month(2019,3))
#%%
try:
    x=0
    y=0
    z=x+z
except:
    w=30
#%%
x=eval(input("請輸入被除數x:"))
y=eval(input("請輸入除數y:"))
z=x/y
print("x除以y的結果等於",z)

try:
    x=eval(input("請輸入被除數x:"))
    y=eval(input("請輸入除數y:"))
    z=x/y
except ZeroDivisionError:
    print("除數不得為0")
except Exception as e1:
    print(e1.args)
else:
    print("沒有捕捉到例外!x除以y的結果等於",z)
finally:
    print("離開try...except區塊")
    
    


        


