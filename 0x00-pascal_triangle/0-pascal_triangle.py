#!/usr/bin/python3

def pascal_triangle(n):
    if n <= 0:
        return []
    if n == 1:
        return [[1]]
    triangle = []
    for i in range(n):
        if len(triangle) <= i:
            arr = [1]
            for j in range(1, i + 1):
                first = 0
                if j - 1 >= 0:
                    first = triangle[i - 1][j - 1]
                second = 0
                if j < len(triangle[i - 1]):
                    second = triangle[i - 1][j]
                arr.append(first + second)
            triangle.append(arr)
    return triangle
