import numpy as np
import time

def getCombo(multiplier) -> list:
    result = [[multiplier[0], multiplier[1], multiplier[2]], [multiplier[0], multiplier[2], multiplier[1]],
              [multiplier[1], multiplier[0], multiplier[2]], [multiplier[1], multiplier[2], multiplier[0]],
              [multiplier[2], multiplier[1], multiplier[0]], [multiplier[2], multiplier[0], multiplier[1]]]

    return result


def hackify():
    
    exit = False
    while not exit:
        nums = input("Please enter numbers:\n")
        multiplier = input("Please enter multiplier:\n")
        target = input("Please enter the target number:\n")

        nums = list(map(int, nums.split(" ")))
        multiplier = list(map(int, multiplier.split(" ")))
        target = int(target)
        
        for m in getCombo(multiplier):
            result = np.dot(nums, np.transpose(m))
            if result == target:
                exit = True
                print(nums[0], "--->", m[0])
                print(nums[1], "--->", m[1])
                print(nums[2], "--->", m[2])
                time.sleep(15)
                break
        if not find:
            print("Please check your input numbers, result DNE")
    

hackify()
