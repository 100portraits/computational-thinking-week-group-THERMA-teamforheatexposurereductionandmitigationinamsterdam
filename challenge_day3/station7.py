def solution_station_7(string):
    a, b, c, d, e = 3, -1, 4, 7, 0.5
    result = eval(string, {"a": a, "b": b, "c": c, "d": d, "e": e})
    
    return float(result)