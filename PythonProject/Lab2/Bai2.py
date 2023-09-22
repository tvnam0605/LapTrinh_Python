
def xuatDSSV(sv):
    for i in lines:
        if i.strip() not in sv:
            sv.append(i.strip())

file = open("Z:\PythonProject\Lab2\sinhvien.txt", "r", encoding="utf8")
lines = file.readlines()
file.close()

dssv = []
xuatDSSV(dssv)

print("Danh sách sinh viên ban đầu:")
for i in dssv:
    print(i)

dssv.sort()
print("\nDanh sách sinh viên sau khi sắp xếp tăng dần theo tên:")
for i in dssv:
    print(i)

dssv.reverse()
print("\nDanh sách sinh viên sau khi sắp xếp giảm dần theo tên:")
for i in dssv:
    print(i)
