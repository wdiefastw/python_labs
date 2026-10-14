a = 12
b = 12.43
c = '12'
d = True
print(a)
12

#n = int(input("Введи число: "))
#m = int(input("Введи число: "))
#print(n+m)
#int()
#float()
#str()
#bool()

#a, b = map(int, input().split())
#print(a + b)

a = int(input())
b = int(input())
c= int(input())
if a > b and a > c:
    print(a)
elif a < b and b > c:
    print(b)
elif c > a and c > b:
    print(c)

print(max(a, b, c))
print(min(a, b, c))
