def prime_numbers():
    prime_list = []

    for i in range(1, 1000):
        value = 0
        for j in range(1, i):
            if i % j == 0:
                value += 1
        if value >= 2:
            continue
        if value < 2:
            prime_list.append(i)
    return prime_list

def palindrome(number):
    temp = number
    rev = 0
    while temp != 0:
        dig = temp % 10
        rev = rev * 10 + dig
        temp = temp // 10
    if number == rev:
        return 1
    else:
        return
if __name__ == "__main__":
    palindrome_list = []
    prime_list = prime_numbers()
    for i in prime_list:
        if palindrome(i):
            palindrome_list.append(i)
    print(prime_list)
    print(palindrome_list)
