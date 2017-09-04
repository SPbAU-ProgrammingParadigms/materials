def guess_number(secret=42):
    while True:
        number = input()
        guess = int(number)
        if guess == secret:
            print('Hooray!')
            break # break out of while loop
        print('Another try')

def fizz_buzz(n):
    for i in range(1, n + 1):
        pass


def dot_product(a, b):
    return sum([i * j for i, j in zip(a, b)])


def hanoi(n, src, dst):
    if n == 0:
        return
    tmp = 3 - src - dst
    hanoi(n - 1, src, tmp)
    print(src, " -> ", dst)
    hanoi(n - 1, tmp, dst)

hanoi(10, 0, 1)
