def getOnlyEvens(nums):
    for i in range(len(nums)):
        if nums[i] % 2 == 0 and i % 2 == 0:
            print(nums[i])
# getOnlyEvens([1, 2, 3, 6, 4, 8])
# getOnlyEvens([0, 1, 2, 3, 4])
def reverseCompare(num):
    reversed_num = num[::-1]
    if (reversed_num > num):
        print("Not ok")
    else:
        print("ok")
# reverseCompare("72")
def returnFactorial(num):
    if num == 0:
        print("1")
    for i in range(1, num):
        num *= i
    print(num)
# returnFactorial(5)
# returnFactorial(6)
def checkMeera(nums):
    factors_of_two = []
    for num in nums:
        factors_of_two.append(num*2)
    # print(factors_of_two)
    for num in nums:
        # print(num)
        if num in factors_of_two:
            return "I am Not a Meera Array"
    return "I am a Meera Array"
        
# print(checkMeera([10, 4, 0, 5]))
# print(checkMeera([7, 4, 9]))
# print(checkMeera([1, -6, 4, -3]))

def isDual(nums):
    # set_of_nums = set(nums)
    num_appear = []

    for num in nums:
        num_appear.append(nums.count(num))

    for num in num_appear:
        if num != 2:
            return "Not Dual"
    return "Dual"
        # print(num)
        # if num in set_of_nums:
        #     num_appear += 1
        # if num_appear != 2:
        #     print("not dual")
        # else:
        #     num_appear = 0
    # print(num_appear)

# print(isDual([1, 2, 1, 3, 3, 2]))
# print(isDual([2, 5, 2, 5, 5]))
# print(isDual([3, 1, 1, 2, 2]))

def digitalClock(second):
    hour = second // 3600
    remaining_hour = second % 3600
    minute = remaining_hour // 60
    remaining_second = minute % 60
    second = remaining_hour % 60

    return f"{hour}:{minute}:{second}"


# print(digitalClock(5025))
# print(digitalClock(61201))
# print(digitalClock(87000))
