#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
演算法第八題a小題
7110064039
徐人豪
"""
import matplotlib.pyplot as plt
import random
import time
import numpy as np

random.seed(0)

n_list = list(range(10, 1000+10, 10))
selected_integers = list(range(1, 10000+1, 1))
search_algorithms = ['linear', 'binary', 'Fibonacci']

mean_execution_time_linear_list = []
mean_execution_time_binary_list = []
mean_execution_time_Fibonacci_list = []


def linear(S, x):
    start = time.time()
    for i in range(len(S)):
        if S[i] == x:
            break

    end = time.time()
    return end-start


def binary(S, x):
    start = time.time()

    low = 0
    upper = len(S) - 1
    while low <= upper:
        mid = int((low + upper) / 2)
        if S[mid] < x:
            low = mid + 1
        elif S[mid] > x:
            upper = mid - 1
        else:
            break
    end = time.time()
    return end-start


def Fibonacci(arr, x):
    start = time.time()

    l = len(arr)
    elim = -1
    fn_2 = 0
    fn_1 = 1
    fn = fn_1+fn_2

    while fn < l:
        fn_1, fn_2 = fn, fn_1
        fn = fn_1+fn_2

    while fn > 1:

        curr = min(elim+fn_2, l-1)

        if arr[curr] == x:
            break

        elif arr[curr] > x:
            fn = fn_2
            fn_1 = fn_1 - fn_2
            fn_2 = fn_2 - fn_1
        else:
            fn = fn_1
            fn_1 = fn_2
            fn_2 = fn - fn_1
            elim = curr

    end = time.time()
    return end-start


def main():
    for n in n_list:

        for method in search_algorithms:
            execute_time_sum = 0
            for times in range(5):
                S = random.sample(selected_integers, n)
                S.sort()
                x = random.sample(selected_integers, 1)[0]

                if method == 'linear':
                    execute_time = linear(S, x)
                elif method == 'binary':
                    execute_time = binary(S, x)
                else:
                    execute_time = Fibonacci(S, x)

                execute_time_sum = execute_time_sum + execute_time
            mean_execuution_time = (execute_time_sum / 5)

            if method == 'linear':
                mean_execution_time_linear_list.append(mean_execuution_time)
            elif method == 'binary':
                mean_execution_time_binary_list.append(mean_execuution_time)
            else:
                mean_execution_time_Fibonacci_list.append(mean_execuution_time)

    plt.plot(np.array(n_list), np.array(
        mean_execution_time_linear_list), label='linear')
    plt.plot(np.array(n_list), np.array(
        mean_execution_time_binary_list), label='binary')
    plt.plot(np.array(n_list), np.array(
        mean_execution_time_Fibonacci_list), label='Fibonacci')

    plt.xlabel("n")
    plt.ylabel("mean execution time")
    plt.legend()
    plt.show()


main()
