def divisible_check(num, divider):
    if num % divider == 0:
        return True
    else:
        return False


n = int(input())
div = int(input())
if divisible_check(n, div):
    print(f"The number {n} is divisible by {div}.")
else:
    print(f"Division is not possible!")
