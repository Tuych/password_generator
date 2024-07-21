from django.shortcuts import render
import random


def main(request):
    select_numbers = [i for i in range(4, 21)]
    ascii_list = [chr(i) for i in range(97, 123)]
    password = ''

    length = int(request.GET.get('length'))

    if request.GET.get('uppercase'):
        ascii_list.extend([chr(i) for i in range(65, 91)])

    if request.GET.get('numbers'):
        ascii_list.extend([chr(i) for i in range(48, 58)])

    if request.GET.get('symbols'):
        ascii_list.extend([chr(i) for i in range(33, 48)])
        ascii_list.extend([chr(i) for i in range(58, 64)])

    for i in range(length):
        password += random.choice(ascii_list)

    context = {
        'select_numbers': select_numbers,
        'password': password,
    }

    return render(request, 'index.html', context)
