digits = []
for i in range(int(input('введите количество цифр '))):
    digits.append(int(input('введите {} цифру'.format((i+1)))))

print(sorted(digits))