def binaryVerify(binNum):
    goodNum = True
    goodNums = ['0','1']
    if len(binNum) != 8:
        goodNum = False
    else:
        for digit in binNum:
            if digit not in goodNums:
                goodNum = False
    return goodNum


def binaryCalc(binNum):
    answer = 0
    binNum = reversed(binNum)

    for index, digit in (enumerate(binNum)):
        if digit == "1":
            answer += (2**index)
    return(answer)



while True:

    binaryInput = input("Enter an 8-digit binary number: ")
    if binaryVerify(binaryInput):
        print(binaryCalc(binaryInput))
    else:
        print("Please enter a valid 8-digit number containing only 1's and 0's.")
