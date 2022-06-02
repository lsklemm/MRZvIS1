from datetime import datetime
from time import perf_counter, perf_counter

# преобразование числа в двоичную систему
def into_binary(decimal_number):
    binary_number=''
    while decimal_number > 0:
        binary_number = str(decimal_number % 2) + binary_number
        decimal_number = decimal_number // 2
    return binary_number


# проверка на 4 разряда
def check_number_digits(number):
    number = str(number)
    if len(number) < 4:
        new_number = ''
        number_start_digit = 4 - len(number)
        # resize the number to be 4 digital
        index = 0
        while index != number_start_digit:
            new_number += '0'
            index += 1
        new_number += number
        number = new_number
        return number
    else:
        return number


# установление одинаковой длины элементов
def check_digits(bigger, smaller):
    bigger_len = len(bigger)
    smaller_len = len(smaller)

    new_value = ''
    for i in range(0, bigger_len - smaller_len):
        new_value += '0'
    smaller = new_value + smaller
    return smaller


# бинарная композиция
def binary_composition(list, my_time):
    result = ''
    if len(list) == 2:
        print('\n\tСумма:')

        carry = 0
        first_number = list[0]
        second_number = list[1]
        if len(first_number) > len(second_number):
            second_number = check_digits(first_number, second_number)
        elif len(second_number) > len(first_number):
            first_number = check_digits(second_number, first_number)

        print('\tПервое слагаемое: ', first_number)
        print('\tВторое слагаемое: ', second_number)
        for i in range(len(first_number) - 1, -1, -1):
            r = carry
            r += 1 if first_number[i] == '1' else 0
            r += 1 if second_number[i] == '1' else 0
            result = ('1' if r % 2 == 1 else '0') + result

            carry = 0 if r < 2 else 1

        if carry != 0:
            result = '1' + result

        my_time.append(datetime.now())
        return str(result)
    else:
        my_time.append(datetime.now())
        return result


# двоичное умножение с промежуточными результатами
# с левым сдвигом частичной суммы
def digital_binary_multiplication(binary_number, digit, sum):
    time1 = perf_counter()

    multiplication_result = ''
    intermediate_sum=''
    binary_number = str(binary_number)

    time = ''
    finish_time = []

    if digit == 1:
        multiplication_result = binary_number
        sum.append(multiplication_result)
        start_time = datetime.now()

        intermediate_sum = str(binary_composition(sum, finish_time))

        time = start_time - finish_time[0]

    elif digit == 0:
        for i in range(0, len(binary_number)):
            multiplication_result += '0'
        sum.append(multiplication_result)

        intermediate_sum = str(binary_composition(sum, finish_time))



    # сдвиг влево
    if len(sum) == 2:
        print('\tЧастичная сумма = ', intermediate_sum)

        sum.clear()
        finish_time.clear()
        intermediate_sum += '0'
        sum.append(intermediate_sum)
    return binary_number

# умножение двух двоичных чисел
def multiplication(first_binary, second_binary):
    print('\n\tПроизведение:\n\t')
    sum=[]

    print('\tПервое число: ', first_binary)
    print('\tВторое число:', second_binary)
    for i in second_binary:
        if i == '0':
            first_binary = digital_binary_multiplication(str(first_binary), 0, sum)
        elif i == '1':
            first_binary = digital_binary_multiplication(str(first_binary), 1, sum)

    end = ''
    end_from_sum = sum[0]
    for i in range(0, len(end_from_sum) - 1):
        end += end_from_sum[i]
    print('\n\t\tРезультат: ', end)
    print('\t')


# функции
def lists_multiplication(first_list, second_list):

    for i in range(0,2):
        first_number = check_number_digits(into_binary(int(check_number_digits(first_list[i]))))
        second_number = check_number_digits(into_binary(int(check_number_digits(second_list[i]))))
        multiplication(first_number, second_number)



lists_multiplication([3, 8], [5, 4])