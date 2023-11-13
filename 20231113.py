num=[]
num1=[1,2.5,"happy"]
num2=(1,2.5,"happy")
num2=list(num2)
#%%
x=[1,4,6,8,10,12,14,16,18,20]
del x[2]
del x[5]
print(x)
#%%
listc=[i for i in range(10)]
print(listc)
listc2=[j+3 for j in range(10)]
print(listc2)

x = [5,10,15,20,25,30,35,40,45,50,55]
x[1:4]
x[3:-2]

print("egg" in ["egg","apple"])
#%%
print(len([1,3,5,7,9]))

print(max([1,3,5,7,9]))

print(min([1,3,5,7,9]))

print(sum([1,3,5,7,9]))
#%%
num1=[1,3,5,7,9]
num2=[2,4,6,8,10]
num1.append(8)
print(num1)
num1.extend(num2)
print(num1)
num1.insert(2,150)
print(num1)
num1.pop()
print(num1)
num1.reverse()
print(num1)
num1.remove(1)
print(num1)
#%%
a=(3,7,5,9)
b=()
c=(2,[3,7],(8,9,10))
d=a[2]
e=a[2:4]
f=c[2][2]
#%%
s1={1,2,3,4,5}
s2={4,5,6,7,8}
print(s1-s2)
#%%
a={1,3,2,4,3,5,7,5,6}
print(len(a))
print(max(a))
print(min(a))
print(sum(a))
#%%
d1 = {"a":50,"b":150}
x={"a":123,"b":456}
y={"b":456,"a":123}
print(x==y)
print(x)
print(y)
#%%
a={"one":1, "two":2, "three":3}
del a ["one"]
print(a)


#%%

