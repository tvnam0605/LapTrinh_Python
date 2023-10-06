soGiay=int(input("Nhập số giây cần đổi:"))
gio=soGiay%86400//3600
phut=soGiay%86400%3600//60
giay=soGiay%86400%3600%60 
time = str(gio)+":"+str(phut)+":"+str(giay)
print(time)