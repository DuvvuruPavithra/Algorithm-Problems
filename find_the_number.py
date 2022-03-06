

def find_number(low, high):
    mid = (low + high )//2
    compare = input(f"Check the value with {mid} 1.Equal\t2.Greater\tS.Smaller: ")
    if compare == "e" or compare == "E":
        print(f"{mid} is your guess Number")
    if compare == "g" or compare == "G":
        find_number(mid, high)
        print("Mid value is:", mid)
        print("High value is:", high)

    if compare == "s" or compare == "S":
        find_number(low, mid)
        print("Low value is:", low)
        print("Mid value is:", mid)


if __name__ == "__main__":
    n = int(input("Enter the value for guess 2**n: "))
    print(f"Think of a number between 0 - {2**n}")
    find_number(1, (2**n)-1)