num_list = [1, 2, 3]
items = iter(num_list)
for i in range(len(num_list)):
    print(f'first items next is: {next(items)}')

print("-----------------------")
for i in range(len(num_list) + 1):
    print(f'second items next is: {next(items)}')
