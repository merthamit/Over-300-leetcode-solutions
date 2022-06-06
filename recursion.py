def powerOfNum(base,power):
    assert base >= 0 and power >= 0 and int(power) == power , 'There is a error. Please give a positive number and power must be positive.' 
    if(power == 0):
        return 1
    if(power == 1):
        return base
    return base * powerOfNum(base, power-1)

def sumOfDigits(num):
    if(num == 0):
        return 0
    return sumOfDigits(int(num / 10)) + num % 10


def fibonacci(num, cache = {}):
    cachedNums = cache or {}
    if(num in cachedNums):
        return cachedNums[num]
    if(num in [0,1]):
        return num
    cachedNums[num] = fibonacci(num - 1, cachedNums) + fibonacci(num - 2, cachedNums)
    return cachedNums[num]

def factorial(num):
    assert int(num) == num and num >= 0, 'There is a error.'
    if(num in [0,1]):
        return 1
    return factorial(num - 1) * num

def gcd(num1, num2):
    assert num1 >= 0 and num2 >= 0, 'Error...'
    if(num2 == 0):
        return num1
    print(num1 % num2)
    return gcd(num2, num1 % num2)    


# def decimalToBinary(num, nums = []):
#     nums.append(num % 2)
#     if(int(num / 2) == 0):
#         nums.reverse()
#         nums = map(str,nums)
#         return ''.join(nums) 
#     return decimalToBinary(int(num / 2), nums)

def decimalToBinary(num):
    assert int(num) == num, 'Must be integer.'
    if(num == 0):
        return 0
    return decimalToBinary(int(num / 2)) * 10 + int(num % 2)


print(decimalToBinary(31))
# print(''.join([1,2,3]))

# gcd(12,24)
# print(fibonacci(5))
# print(powerOfNum(2,5))
# print(sumOfDigits(1124))
# print(factorial(5))


# print(11 / 10)
# print(11 % 10)
