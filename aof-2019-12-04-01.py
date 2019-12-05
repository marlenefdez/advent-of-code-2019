# advent of code, day 4, puzzle 1

def find_count_possible_passwords(min_n, max_n):
    count = 0
    for num in range(min_n, max_n+1):
        if two_consec_digits(num) and all_digits_increase(num):
            count += 1
    return count

def all_digits_increase(num):
    num = str(num)
    for i, digit in enumerate(num[:-1]):
        if num[i] > num[i+1]:
            return False
    return True

def two_consec_digits(num):
    num = str(num)
    for i, digit in enumerate(num[:-1]):
        if num[i] == num[i+1]:
            return True
    return False



if __name__ == "__main__":
    num = find_count_possible_passwords(278384, 824795)
    print('The total number of possible passwords is {}'.format(num))

