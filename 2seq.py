list_input =  input('введите несколько цифр через запятую ').replace(' ',',').replace('/',',').split(',')
list_digit = []
for i, number in enumerate(list_input):
    try:
        list_digit.append(int(number))
    except:
        continue
list_set_digit = set(list_digit)
print(list_set_digit)
