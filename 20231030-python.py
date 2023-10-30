with open("writedata.txt","w") as file:
    file.write("阿囉哈\n")
    file.write("ABC\n")
    file.write("0800")




with open("writedata.txt","r") as file:
    data = file.read()
    print(data)

