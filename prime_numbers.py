def prime_numbers():
    total_list = []
    for number in range(1, 1000):
        if number > 1:
            for i in range(2, number):
                if (number % i) == 0:
                    break
            else:
                print(number)
    return total_list.append(number)
prime_numbers()

