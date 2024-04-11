def encode(n):
    my_list = []
    new_list = []
    str_out = ''
    for i in n:
        my_list.append(int(i))

    for num in my_list:
        if num < 7:
            new_list.append(num+3)
        else:
            new_list.append((num+3)%10)

    for num in new_list:
        str_out += str(num)

    return str_out

