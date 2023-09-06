def solution_station_4(i):
    return is_prime(i)

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


for i in range(0, 25):
    print(solution_station_4(i))