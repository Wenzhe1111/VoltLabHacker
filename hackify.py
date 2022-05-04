import numpy as np


def getCombo(multiplier) -> list:
    result = [[multiplier[0], multiplier[1], multiplier[2]], [multiplier[0], multiplier[2], multiplier[1]],
              [multiplier[1], multiplier[0], multiplier[2]], [multiplier[1], multiplier[2], multiplier[0]],
              [multiplier[2], multiplier[1], multiplier[0]], [multiplier[2], multiplier[0], multiplier[1]]]

    return result


def hackify():
    confirm = False

    while not confirm:

        nums = input("Please enter numbers:\n")
        multiplier = input("Please enter multiplicators:\n")
        target = input("Please enter the target number:\n")
        print("The numbers are ", nums)
        print("The multiplicators are ", multiplier)
        print("The target is ", target)
        io = input("Please confirm the results by pressing y:\n")
        if io == "y":
            confirm = True
    nums = list(map(int, nums.split(" ")))
    multiplier = list(map(int, multiplier.split(" ")))
    target = int(target)
    for m in getCombo(multiplier):
        result = np.dot(nums, np.transpose(m))
        if result == target:
            for i in range(len(nums)):
                print(nums[i], "---->", m[i])
            break


hackify()
