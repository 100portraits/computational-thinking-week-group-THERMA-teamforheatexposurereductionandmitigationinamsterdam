# dictionary used for (small) optimisation purposes
fibonacci_dict = {}
i = 1

def solution_station_1(input):
    if input <= 0:
        return
    
    elif input <= 2:
        output = 1
        if input not in fibonacci_dict:
            fibonacci_dict[input] = output
    
    elif input > 1:
        if input in fibonacci_dict:
            output = fibonacci_dict[input]
        else:
            val1 = solution_station_1(input-1)
            val2 = solution_station_1(input-2)
            output = val1 + val2

        if input not in fibonacci_dict:
            fibonacci_dict[input] = output

    return int(output)