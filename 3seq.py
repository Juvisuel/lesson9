list1_input =  input('введите несколько цифр через запятую ').replace(' ',',').replace('/',',').split(',')
list2_input =  input('введите еще несколько цифр через запятую ').replace(' ',',').replace('/',',').split(',')
List_differ = set(list1_input)-set(list2_input)
print(List_differ)