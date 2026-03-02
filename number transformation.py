# Read input number
N = int(input())

while (N>0):
    print(N, end ="")
    if (N==1):
        break 
    elif N % 2 == 0:
        N = N // 2
    else:
        N = 3 * N + 1

