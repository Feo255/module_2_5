def get_matrix(n, m, value):
    set = []
    result = []
    for i in range(m):
        set.append(value)
    for k in range(n):
        result.append(set)
    return(result)
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)