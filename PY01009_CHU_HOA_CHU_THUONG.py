s = input()
chuHoa = 0
chuThuong = 0
for c in s:
    if c.islower():
        chuThuong += 1
    if c.isupper():
        chuHoa += 1

if chuThuong >= chuHoa:
    print(s.lower())
else:
    print(s.upper())