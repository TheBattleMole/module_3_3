def print_params(a=1, b="Строка", c=True):
    print(a, b, c)


print_params()
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [1, "Hello", True]
values_dict = {'a': 2, 'b': "GoodBye", 'c': False}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = [89, "'How are you'"]
print_params(*values_list_2, 42)