def sayhello(num):
    print("hello!")
    print("hello!")
    print("hello!")
    
sayhello(1.5>2)
#print("Time 1")
#sayhello()
#print("Time 2")
#sayhello()
#print("Time 3")
#%%
def CtoF1(degreeC):
    degreeF = degreeC * 1.8 +32
    print("攝氏",degreeC,"度可以轉化成華式",degreeF,"度")
temperatureC = eval(input("請輸入攝氏溫度:"))
CtoF1(temperatureC)
#%%
def teatime(dessert,drink = "綠茶"):
    print("我的甜點:",dessert,";飲料:", drink, sep="")
teatime("千層蛋糕","紅茶")
teatime("貝果")
teatime(drink = "牛奶", dessert = "熱壓三明治")
teatime("帕尼尼", drink = "鮮奶茶")
#%%
def cal(x,y):
    div = x // y
    mod = x % y
    return(div, mod)
a, b = cal(150, 7)
print("150除以7的商數為", a, "，餘數為", b)
c, d = cal(230, 12)
#%%
score = eval(input("請輸入國文分數(0~100):"))
if score >= 60:
    print("及格!")
else:
    print("不及格!")
#%%
score = eval(input("請輸入國文分數(0~100):"))
if score >= 90:
    print("優等")
elif score >= 80:
    print("甲等")
elif score >= 70:
    print("乙等")
elif score >= 60:
    print("丙等")
else:
    print("不及格")
#%%

    
print("230除以12的商數為", c, "，餘數為", d)