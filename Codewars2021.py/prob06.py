num = (input())
words = input().split()

result = []
for i in words:
    for letter in i:
        e = ord(str(letter))
        d = chr(e - 5)
        if d == '=': 
            d = chr(e + 21)
        result.append(d)
for i in words:
    print(i)
print(result)
