def solution_station_4(i):
    return is_prime(i)

def is_prime(i):
    if i <= 1:
        return False
    elif i <= 3:
        return True
    elif i % 2 == 0 or i % 3 == 0:
        return False
    else:
        divisor = 5
        while divisor * divisor <= i:
            if i % divisor == 0 or i % (divisor + 2) == 0:
                return False
            divisor += 6
        return True



for i in range(0, 23):
    print(solution_station_4(i))